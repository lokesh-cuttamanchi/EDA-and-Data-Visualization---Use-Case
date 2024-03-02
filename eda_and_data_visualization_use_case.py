# -*- coding: utf-8 -*-
"""EDA and Data Visualization - Use Case.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z_mQdRuJIR7bJtgo1bzNue6XeuKnyl_A

# Exploratory Data Analysis (EDA):

Exploratory Data Analysis is all about analyzing the dataset and summarizing the key insights and characteristics of the data.


**EDA checklist:**
1.	Understanding the dataset, and its shape
2.	Checking the data type of each columns
3.	Categorical & Numerical columns
4.  Checking for missing values
5.	Descriptive summary of the dataset
6.	Groupby for classification problems

Importing Libraries
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

"""Data Collection

"""

# loading the breast cancer dataset from csv file to pandas data frame
cancer_data = pd.read_csv('/content/data.csv')

"""# **Exploratory Data Analysis**

"""

# printing the first five rows of the dataframe
cancer_data.head()

# removing the unnamed column
cancer_data.drop(columns='Unnamed: 32' , axis = 1 , inplace=True)

cancer_data.head()

# checking the data types
cancer_data.info()

"""Diagnosis column is a CATEGORICAL columnm whereas remIning are continuous values

"""

# removing the id column
cancer_data.drop(columns='id', axis = 1, inplace=True)

cancer_data.describe()

cancer_data.diagnosis.unique()

cancer_data.shape

# checking for missing values
cancer_data.isnull().sum()

#Statistical summary of the data - Descriptive Statistics
cancer_data.describe()

#Checking the distribution of target Variable
cancer_data['diagnosis'].value_counts()

# encoding the target column
label_encode = LabelEncoder()
labels = label_encode.fit_transform(cancer_data['diagnosis'])
cancer_data['target'] = labels

cancer_data.head()

cancer_data.drop(columns = 'diagnosis', axis=1, inplace=True)

# diagnosis column removed
cancer_data

cancer_data['target'].value_counts()

"""Benign --> 0

Malignant --> 1
"""

#Grouping the data based on the target
cancer_data.groupby('target').mean()

"""We can clearly see that for most of the features, the mean values are higher for Malignant(1) cases and lower for Benign(0) cases

# **Summary from EDA:**


1. No missing Values
2. All are continuous numerical values except for Target column
3. Mean is slightly more than the median for most of the features. So it is right skewed.
4. Slight imbalance in the dataset Benign(0) cases are more than Malignant(1) cases
5. Mean of most features are clearly larger for Malignant cases compared to the benign cases (Groupby)

# **Data Visulization**
"""

# countplot for the target column for checkin gthe distribution of target
sns.countplot(x= 'target', data=cancer_data)

# this is how we can get all the column names of the dataframe
for column in cancer_data:
  print(column)

# creating a for loop to get the distribution plot for all columns
for column in cancer_data:
  sns.displot(x=column, data=cancer_data)

sns.distplot(x=cancer_data.radius_mean)

"""we can also use pairplot for checking relationship between features but it will take all the features and we have 30 and 30x30 is 900 so we are doing for only two feature.


**Scatter plot of first 2 columns**
"""

# Select first column of the dataframe as a series
first_column = cancer_data.iloc[:, 0]

# Select second column of the dataframe as a series
second_column = cancer_data.iloc[:, 1]

print(first_column)
print('-----')
print(second_column)

plt.scatter(x=first_column,y=second_column)

"""**Outliers Detection**

box plot for visualizing the outliers in the dataset
"""

for column in cancer_data:
  plt.figure()
  cancer_data.boxplot([column])

"""# Correlation Matrix"""

correlation_matrix = cancer_data.corr()

# constructing a heat map to visualize the correlation matrix
plt.figure(figsize=(20,20))
sns.heatmap(correlation_matrix, cbar=True, fmt='.1f', annot=True, cmap='Blues')
plt.savefig('Correlation Heat map')

"""Multicollinearity problem:

Multicollinearity exists when an independent variable is highly correlated with one or more independent variables

We can remove the features if they have high +ve or -ve correlation between them

**Inference from EDA & Data Visualization:**
1. No missing Values
2. All are continuous numerical values except for Target column
3. Mean is slightly more than the median for most of the features. So it is right skewed.
4. Slight imbalance in the dataset Benign(0) cases are more than Malignant(1) cases
5. Mean of most features are clearly larger for Malignant cases compared to the benign cases (Groupby)
6. Most of the features have Outliers
7. Correlation Matrix reveal that most of the features are highly correlated. So we can remove certain features during Feature Selection
"""