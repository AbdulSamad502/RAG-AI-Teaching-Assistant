import os
import requests
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })
    embedding=r.json()["embeddings"]
    return embedding
def inference(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={
        "model":"llama3.2",
        "prompt":prompt,
        "stream":False
    })
    response=r.json()
    return response




df=joblib.load("embeddings.joblib")
incomming_query=input("Ask a question:-")
query_to_vector=create_embedding([incomming_query])[0]
Cosine_similarity1=cosine_similarity(np.vstack(df["embedding"]),[query_to_vector]).flatten()

top_res=30
max_idx=Cosine_similarity1.argsort()[::-1][0:top_res]

newdf=df.iloc[max_idx]

prompt=f""" I am teaching web development course in my  Sigma Web development course . Here in this video subtitle chunks containing video title ,video number,start time in seconds,end time in second, title at that time:
{newdf[["title","number","start","end","text"]].to_json(orient="records")}
----------------------------------------
"{incomming_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format ,its just for you ) where and how much content is thouugh in this video(in which video at what timestamp) and guide the user to go to the perticular video.If user ask unrelated question ,tell him that you can only answer this question related to the course
"""
with open("prompt.txt","w") as f:
    f.write(prompt)
response=inference(prompt)["response"]
print(response)
with open("response.txt","w") as f:
    f.write(response)
    
# for index,items in newdf.iterrows():
#     print(index,items["title"],items["number"],items["text"],items["start"],items["end"])

        
