# all the imports required
import numpy as np
import pandas as pd
import time
import json
import datetime


# To fetch IDs of the story's
import requests
url="https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
data=response.json()
data

# Append in to a list l
l=[]
headers = {"User-Agent": "TrendPulse/1.0"}
for id in data:
    try:
        url=f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        time.sleep(0.2)
        response=requests.get(url,headers=headers,timeout=2)
        l.append(response.json())
    except Exception as e:
        print(f"Failed  Id = {id} by  {e}")
        continue

# Converting list into Dataframe
df=pd.DataFrame(l)

# Removing unwanted columes
df=df.drop(columns=['kids','type','text','url','time'],axis=1)


technology = ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"]
worldnews = ["war", "government", "country", "president", "election", "climate", "attack", "global"]
sports = ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"]
science = ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"]
entertainment = ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]

# checking what category it belongs
df['category']='other'
df.loc[df['title'].str.contains('|'.join(technology),case=False,na=False),'category']="technology"
df.loc[df['title'].str.contains('|'.join(worldnews),case=False,na=False),'category']="worldnews"
df.loc[df['title'].str.contains('|'.join(entertainment),case=False,na=False),'category']="entertainment"
df.loc[df['title'].str.contains('|'.join(sports),case=False,na=False),'category']="sports"
df.loc[df['title'].str.contains('|'.join(science),case=False,na=False),'category']="science"

# removing other category rows
df=df[df['category']!="other"]

# Grouping by category and only selecting max of 25 rows of each group
df=df.groupby('category').head(25)
df=df.reset_index(drop=True)

# Adding date and time column as asked in the task
df['collected_at']=datetime.datetime.now()

# ordering the columns
df=df[['id','title','category','score','descendants','by','collected_at']]

# Creating a json file inside the data folder by converting df to json
df.to_json("data/trends20260406.json",orient='records',indent=4)