# -*- coding: utf-8 -*-
"""Mall_Customers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZmeoIsfkiGbJbGeUl3Dxm0mdB4Gu7-0i
"""

from google.colab import drive

import pandas as pd

path = "/content/drive/MyDrive/Mall_Customers.csv"
df = pd.read_csv(path)

#load the dataset

df.head()

import seaborn as sns
import numpy as np
import pandas as pd

### Univariate analysis

sns.boxplot(df.Age) # numeric
sns.distplot(df.CustomerID)
sns.countplot(df.Gender) # categorical

## Bivariate analysis

df.plot.scatter('Age','CustomerID')

## Multivariate analysis

sns.pairplot(df)

df.shape

df.info()

df.isnull().any()

#Perform descriptive statistics on the dataset

df.describe()

#Check for Missing values and deal with them

df.isna()

df.isnull().sum()

#Find the outliers and replace them outliers

sns.boxplot(x=df['Age'])

#Check for Categorical columns and perform encoding

x = 'Male'
y = 'Female'
df['Gender'].replace({'M':y, 'F':x})
df

df.tail()

#Scaling the Data

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

x = df[['Age']]
scaledx = scale.fit_transform(x)
print(scaledx)

#Clustering Algorithms

from sklearn import datasets

import warnings
warnings.filterwarnings('ignore')

df=datasets.load_iris()
dir(datasets)