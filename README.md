# 基于多模型协同过滤的机器学习方法

## 项目概述
本项目致力于开发一个餐厅评分预测算法，专注于通过多种机器学习技术对Yelp数据集上的餐厅进行评分预测。我们使用了包括奇异值分解SVD、余弦相似度、交替最小二乘法ALS、随机梯度下降SGD和随机森林等方法，以提供准确的评分预测并增强推荐系统的性能。

## 项目配置方法

1. **（推荐）安装Anaconda**

   - 访问Anaconda官方网站：[www.anaconda.com](https://www.anaconda.com)，从[下载页面](https://www.anaconda.com/download)获取安装程序。
   - 如果在**中国大陆**，由于网络问题，建议使用[清华大学Anaconda镜像站点](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)进行下载。
   - 完成安装后，按照[这个教程](https://blog.csdn.net/weixin_43914658/article/details/108785084)来配置环境变量，以确保可以从命令行运行Anaconda。

2. **进入项目目录**

   - 使用命令行界面，导航到您的项目文件夹。

3. **创建并激活虚拟环境**

   - 创建虚拟环境：在命令行中输入以下命令：

     ```bash
     conda create -n Yelp_env python=3.11
     ```

   - 激活虚拟环境：

     ```bash
     conda activate Yelp_env
     ```

4. **安装项目依赖**

   - 使用pip安装依赖。在项目目录中，有[`requirements.txt`](./requirements.txt)文件，列出了所有必需的Python库，使用以下命令安装依赖：

     ```bash
      pip install -r requirements.txt
     ```
     
   - 如果在**中国大陆**，考虑使用[清华大学PyPI镜像](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)加速依赖安装：
   
  ```bash
     pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

## 项目结构
```bash
$ tree
.
├── README-SC.md
├── README.md
├── assets
│   ├── Palette.json
│   ├── PingFang.ttc
│   ├── yelp_business_dtype.json
│   └── yelp_dtype.json
├── data
│   ├── README-SC.md
│   ├── README.md
│   ├── Yelp_final.csv
│   ├── yelp_academic_dataset_business.csv
│   └── yelp_academic_dataset_review.csv
├── images
│   ├── 01_每个城市的商家数量.png
│   ├── 02_最受欢迎的商家类别.png
│   ├── 03_城市和商家类别组合数量.png
│   ├── 04_获得评论最多的城市和商家类别组合.png
│   ├── Phoenix
│   │   ├── 01_SVD奇异值分布_前20个主成分.png
│   │   ├── 02_不同奇异值数量下的训练集和验证集误差.png
│   │   ├── 03_不同奇异值数量下验证集误差.png
│   │   ├── 04_前两个主成分散点图.png
│   │   ├── 05_去除偏差后的SVD_奇异值分布（前1000个）.png
│   │   ├── 06_去除偏差后SVD_验证集重构误差.png
│   │   ├── 07_去除偏差后的SVD_奇异值分布.png
│   │   ├── 08_去除偏差后的SVD_验证集重构误差.png
│   │   ├── 09_余弦相似度模型_不同K值对评分预测MSE的影响.png
│   │   ├── 10_ALS_特征数量与均方误差的关系.png
│   │   ├── 11_ALS_正则化系数对MSE的影响.png
│   │   ├── 12_带偏差修正的SGD_MSE与迭代次数的关系.png
│   │   └── 13_带偏差修正的SGD_特征数量与MSE关系.png
│   └── Scottsdale
│       ├── 01_SVD奇异值分布_前20个主成分.png
│       ├── 02_不同奇异值数量下验证集误差.png
│       ├── 03_不同奇异值数量下验证集误差.png
│       ├── 04_前两个主成分散点图.png
│       ├── 05_去除偏差后的SVD_奇异值分布（前1000个）.png
│       └── 06_去除偏差后的SVD_验证集重构误差.png
├── notebooks
│   ├── 01_数据预处理.ipynb
│   ├── 02_Phoenix餐厅.ipynb
│   └── 03_Scottsdale餐厅.ipynb
├── reference
│   ├── 1404.1100v1.pdf
│   ├── Wikipedia.md
│   ├── 奇艺值分解.md
│   ├── 【学长小课堂】什么是奇异值分解SVD--SVD如何分解时空矩阵.mp4
│   └── 【学长小课堂】什么是奇异值分解SVD--SVD如何分解时空矩阵.srt
└── src
    ├── __init__.py
    ├── color_generator.py
    ├── evaluation.py
    ├── model.py
    └── preprocessing.py

9 directories, 47 files
```

## 贡献者

[孙逸青](mailto:william_syq@tju.edu.cn)

[张颢南](mailto:shu_1294491613@tju.edu.cn)

