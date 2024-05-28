import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix, lil_matrix


def get_top_m_num_reviews_for_city_and_business(df, m):
    """
    获取按城市和分类统计的商家数量，并返回前m个结果。

    Args:
        df (pd.DataFrame): 包含商家信息的数据框。
        m (int): 要返回的前m个结果的数量。

    Returns:
        pd.Series: 包含前m个按城市和分类统计的商家数量的Series。
    """
    # 创建business_city_count字典，用于存储城市和分类的商家数量
    business_city_count = {}
    n = len(df)

    # 遍历数据框的每一行
    for i in range(n):
        # 获取分类并拆分为列表
        categories = str(df.categories.iloc[i]).split(',')
        # 获取城市名称
        city = df.city.iloc[i]
        # 遍历每个分类
        for category in categories:
            key = (category, city)  # 创建分类和城市的元组
            # 如果元组不存在于字典中，则初始化为1，否则加1
            if key not in business_city_count.keys():
                business_city_count[key] = 1
            else:
                business_city_count[key] += 1

    # 将字典转换为Series并排序
    business_city_count_series = pd.Series(business_city_count)
    business_city_count_series.sort_values(ascending=False, inplace=True)

    return business_city_count_series[:m]


def get_clean_df(df, cols, min_user_review=30, min_res_review=0):
    """
    清洗数据并根据最小评论数量进行过滤

    参数:
        df (DataFrame): 原始数据框
        cols (list): 需要保留的列名列表
        min_user_review (int, 可选): 用户最少评论数，默认值为30
        min_res_review (int, 可选): 商家最少评论数，默认值为0

    返回:
        DataFrame: 清洗并过滤后的数据框
    """
    # 使用.copy()避免SettingWithCopyWarning
    df_new = df[cols].copy()
    # 删除任何包含缺失值的行
    df_new.dropna(axis=0, how='any', inplace=True)

    # 计算每个商家的评论数，并过滤评论数不满足条件的商家
    df_new[cols[1] +
           '_freq'] = df_new.groupby(cols[1])[cols[1]].transform('count')
    df_clean = df_new[df_new[cols[1] + '_freq'] >= min_res_review]

    # 计算每个用户的评论数，并过滤评论数不满足条件的用户
    df_clean[cols[0] +
             '_freq'] = df_clean.groupby(cols[0])[cols[0]].transform('count')
    df_clean_2 = df_clean[df_clean[cols[0] + '_freq'] >= min_user_review]

    return df_clean_2


def get_sparsity(sparse_matrix):
    """
    计算稀疏矩阵的稀疏度

    参数:
        sparse_matrix (csr_matrix): 稀疏矩阵

    返回:
        float: 稀疏度，表示为稀疏矩阵中非零元素的比例
    """
    density = sparse_matrix.nnz / \
        (sparse_matrix.shape[0] * sparse_matrix.shape[1])
    return 1 - density


def get_sparse_matrix(df):
    """
    将数据框转换为稀疏评分矩阵

    参数:
        df (DataFrame): 包含用户、商家和评分的数据框

    返回:
        csr_matrix: 稀疏评分矩阵
    """
    # 获取唯一用户ID列表
    unique_users = list(df['user_id'].unique())
    # 获取唯一商家ID列表
    unique_businesses = list(df['business_id'].unique())
    # 获取评分数据
    ratings = df['stars'].tolist()

    # 将用户ID映射到稀疏矩阵的行索引
    user_indices = pd.Categorical(df['user_id'], categories=unique_users).codes
    # 将商家ID映射到稀疏矩阵的列索引
    business_indices = pd.Categorical(
        df['business_id'], categories=unique_businesses).codes

    # 创建稀疏评分矩阵
    sparse_matrix = csr_matrix((ratings, (user_indices, business_indices)),
                               shape=(len(unique_users), len(unique_businesses)))
    return sparse_matrix


def train_val_test_split(sparse_matrix, num_review_val=2, num_review_test=2):
    """将稀疏矩阵划分为训练集、验证集和测试集

    Args:
        sparse_matrix (csr_matrix): 输入的稀疏矩阵
        num_review_val (int, optional): 每个用户用于验证的评论数. 默认为2.
        num_review_test (int, optional): 每个用户用于测试的评论数. 默认为2.

    Returns:
        tuple: 包含训练集、验证集和测试集的稀疏矩阵
    """
    # 获取非零元素的行索引和列索引
    nonzero_rows, nonzero_cols = sparse_matrix.nonzero()

    # 初始化训练集、验证集和测试集稀疏矩阵
    sparse_matrix_test = csr_matrix(sparse_matrix.shape)
    sparse_matrix_val = csr_matrix(sparse_matrix.shape)
    sparse_matrix_train = sparse_matrix.copy()

    num_users = sparse_matrix.shape[0]  # 用户数

    for user in range(num_users):
        # 获取该用户的所有评论索引
        user_review_indices = nonzero_cols[np.where(nonzero_rows == user)]

        # 打乱索引顺序
        np.random.shuffle(user_review_indices)

        # 划分测试集和验证集索引
        test_indices = user_review_indices[-num_review_test:]
        val_indices = user_review_indices[-(num_review_val +
                                            num_review_test):-num_review_test]

        # 将测试集和验证集的索引设置到对应的稀疏矩阵中
        sparse_matrix_test[user,
                           test_indices] = sparse_matrix[user, test_indices]
        sparse_matrix_val[user, val_indices] = sparse_matrix[user, val_indices]

        # 从训练集中移除验证集和测试集的索引
        sparse_matrix_train[user, test_indices] = 0
        sparse_matrix_train[user, val_indices] = 0

    # 重新创建训练集稀疏矩阵以去除零元素
    train_data = np.array(
        sparse_matrix_train[sparse_matrix_train.nonzero()])[0]
    train_rows = sparse_matrix_train.nonzero()[0]
    train_cols = sparse_matrix_train.nonzero()[1]
    matrix_size = sparse_matrix_train.shape

    sparse_matrix_train = csr_matrix(
        (train_data, (train_rows, train_cols)), shape=matrix_size)

    # 确保训练集、验证集和测试集没有重叠
    overlap_val_test = sparse_matrix_train.multiply(sparse_matrix_val)
    overlap_all = overlap_val_test.multiply(sparse_matrix_test)

    assert overlap_all.nnz == 0, "训练集、验证集和测试集之间存在重叠元素"

    return sparse_matrix_train, sparse_matrix_val, sparse_matrix_test
