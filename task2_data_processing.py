import pandas as pd

# Load json file from data folder and convert to dataframe
df=pd.read_json("data/trends20260406.json",orient="records")
print(len(df))
# To remove duplicate rows by post_id
df=df.drop_duplicates(subset=['post_id'])
print("After removing duplicates: ",len(df))

# To remove rows having null values in columns post_id,title and score (if any one column has it drops)
df.dropna(subset=['post_id','title','score'])
print("After removing nulls: ",len(df))

# To remove the rows which has less score ,less then are equal to 5 (Only taking rows with more then 5 score)
df=df[df['score']>5]
print("After removing low scores: ",len(df))


# To strip the extra space from the title column (Using loc we can modify df)
df.loc[:,'title']=df['title'].str.strip()

# To convert  the DataFrame to a CSV file inside the data folder
df.to_csv("data/trends_clean.csv")
print(f"Saved {len(df)} rows to data/trends_clean.csv")

print("Stories per category:")
print(df['category'].value_counts())