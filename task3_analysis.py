import numpy as np
import pandas as pd

# csv loaded
df=pd.read_csv("data/trends_clean.csv")

# Shape of df
print("Shape of csv :",df.shape)

# Avg of score
print("Average of score :",df['score'].mean())

# Avg of num_comments
print("Average of num_comments :",df['num_comments'].mean())

# numpy states
print("--- NumPy Stats ---")
print("Mean score   :",df['score'].mean())
print("Median score :",df['score'].median())
print("Std deviation:",df['score'].std())
print("Max score    :",df['score'].max())
print("Min score    :",df['score'].min())

# To find most numbe of rows in which category and its number count
high_cate, num_values = df.groupby('category')['score'].count().reset_index().iloc[0]
print(f"Most stories in: {high_cate} ({num_values} stories)")

# most comment story and its number count
n=df['score'].max()
pop_title=df[df['score']==n]['title'].iloc[0]
print(f'Most commented story:"{pop_title}" - {n} comments')

# added new columns
df['engagement']=df['num_comments'] / (df['score'] + 1)
df['is_popular']=np.where(df['score']>df['score'].mean(),True,False)

# Creating CSV file store in data folder
df.to_csv("data/trends_analysed.csv")
print(" final CSV file store in data/trends_analysed.csv")