# Machine Learning Approaches Based on Multi-Model Collaborative Filtering

## Project Overview
This project is dedicated to developing a restaurant rating prediction algorithm, focusing on predicting restaurant ratings on the Yelp dataset using a variety of machine learning techniques. We employ methods including Singular Value Decomposition (SVD), Cosine Similarity, Alternating Least Squares (ALS), Stochastic Gradient Descent (SGD), and Random Forests to provide accurate rating predictions and enhance the performance of recommendation systems.

## Project Setup Method

1. **(Recommended) Install Anaconda**

   - Visit the official Anaconda website: [www.anaconda.com](https://www.anaconda.com), and obtain the installer from the [download page](https://www.anaconda.com/download).
   - If in **mainland China**, due to network issues, it is recommended to download from the [Tsinghua University Anaconda mirror site](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/).
   - After installation, follow [this tutorial](https://blog.csdn.net/weixin_43914658/article/details/108785084) to configure the environment variables, ensuring Anaconda can be run from the command line.

2. **Enter the Project Directory**

   - Use the command line interface to navigate to your project folder.

3. **Create and Activate a Virtual Environment**

   - To create a virtual environment, enter the following command in the command line:

     ```bash
     conda create -n Yelp_env python=3.11
     ```

   - To activate the virtual environment:

     ```bash
     conda activate Yelp_env
     ```

4. **Install Project Dependencies**

   - Install dependencies using pip. In the project directory, there is a [`requirements.txt`](./requirements.txt) file listing all required Python libraries, use the following command to install dependencies:

     ```bash
      pip install -r requirements.txt
     ```
   
   - If in **mainland China**, consider using the [Tsinghua University PyPI mirror](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/) to speed up dependency installation:
   
  ```bash
     pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

## Contributors

[William Sun](mailto:william_syq@tju.edu.cn)

[Haonan Zhang](mailto:shu_1294491613@tju.edu.cn)