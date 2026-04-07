import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("data/trends_analysed.csv")

df=df.sort_values('score',ascending=False)
plt.barh(df['title'].head(10).str.slice(0,50),df['score'].head(10))
plt.title("Title VS Score")
plt.xlabel("Score")
plt.ylabel("Titles")
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

df1=df.groupby('category')['title'].count().reset_index()
plt.bar(df1['category'],df1['title'],color=['red','green','yellow','pink','blue'])
plt.title("Numer of titles in each category")
plt.xlabel("Category")
plt.ylabel("Number of Titles")
plt.savefig("outputs/chart2_categories.png")
plt.show()


m=df['score'].mean()
high=df[df['score']>m]
low=df[df['score']<=m]
plt.scatter(high['score'],high['num_comments'],c='red',label="Popular")
plt.scatter(low['score'],low['num_comments'],c='blue',label="Not Popular")
plt.title("Scatter for score an number of comments")
plt.xlabel("Scores")
plt.ylabel("Number of comments")
plt.legend()
plt.savefig("outputs/chart3_categories.png")
plt.show()


fig, a = plt.subplots(3, 1,figsize=(10,13))

# plot 1
df=df.sort_values('score',ascending=False)
a[0].barh(df['title'].head(10).str.slice(0,50),df['score'].head(10))
a[0].set_title("Title VS Score")
a[0].set_xlabel("Scores")
a[0].set_ylabel("Titles")


# plot 2
df1=df.groupby('category')['title'].count().reset_index()
a[1].bar(df1['category'],df1['title'],color=['red','green','yellow','pink','blue'])
a[1].set_title("Numer of titles in each category")
a[1].set_xlabel("Category")
a[1].set_ylabel("Number of Titles")

# plot 3
m=df['score'].mean()
high=df[df['score']>m]
low=df[df['score']<=m]
a[2].scatter(high['score'],high['num_comments'],c='red',label="Popular")
a[2].scatter(low['score'],low['num_comments'],c='blue',label="Not Popular")
a[2].set_title("Scatter for score an number of comments")
a[2].set_xlabel("Scores")
a[2].set_ylabel("Number of comments")
a[2].legend()

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()