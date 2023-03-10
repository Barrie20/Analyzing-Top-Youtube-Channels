# -*- coding: utf-8 -*-
"""YoutubeProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WCwtfCXYptfNUWEGZkBhxBJ_g5kG_CdG
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/topSubscribed.csv');

data.describe()

data.describe()

data.shape

data.isna().sum()

data.isnull().sum()

data.dtypes

data['Category'].value_counts()      # Breakdown by Category

data = data.replace(',','', regex=True)      # Removing delimeters


# Converting strings to integers
data[['Subscribers','Video Views','Video Count']] = data[['Subscribers','Video Views','Video Count']].astype(int)

data.dtypes # View changes

# Removing URL category
data = data[data.Category != 'https://us.youtubers.me/global/all/top-1000-most_subscribed-youtube-channels']

data['Category'].value_counts() # Breakdown by Category

# Channel with highest views
data.iloc[data['Video Views'].argmax()]

plt.figure(figsize=(9,6))
plt.title("Distribution of Channels, by Subscribers")
plt.ticklabel_format(style='plain', axis='x')
sns.boxplot(x=data['Subscribers'])
plt.show()

plt.figure(figsize=(9,6))
plt.title("Distribution of Channels, by Video Views")
plt.ticklabel_format(style='plain', axis='x')
sns.boxplot(x=data['Video Views'])
plt.show()

plt.figure(figsize=(12,8))
plt.title("Distribution of Channels, by Video Count")
sns.boxplot(x=data['Video Count'])
plt.show()

# New dataframe to hold category value count
df_byCat = data['Category'].value_counts().to_frame('Count').rename_axis('Category').reset_index()

df_byCat

top5 = data["Category"].value_counts().head(5)

plt.figure(figsize=(12,10))

ax = sns.countplot(x=data["Category"],order=top5.index)
ax.bar_label(ax.containers[0])
plt.show()

labels = df_byCat['Category']
plt.figure(figsize=(12,9))
plt.pie(df_byCat['Count'], autopct='%1.1f%%',shadow=False, startangle=90)
plt.axis('equal')
plt.show()