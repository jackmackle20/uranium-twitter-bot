import pandas as pd
import numpy as np 
import sqlite3
import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
from datetime import datetime

tempd_path = os.path.dirname(os.path.realpath("logs"))
tempd_filename = os.path.join(tempd_path, "logs/tempd.txt")

with open(tempd_filename, "r") as t:
    date = t.readlines()[0]
    
db_path = os.path.dirname(os.path.realpath("storage/storage.db"))
db_filename = os.path.join(db_path, "storage.db")

conn = sqlite3.connect(db_filename)

df = pd.read_sql_query("SELECT created_at, full_text FROM tweets WHERE created_at LIKE ?",
                       conn,
                       params=(str(date) + "%",))
conn.close()

sid = SentimentIntensityAnalyzer()
full_text = df["full_text"].tolist()
polarity_scores = list(map(sid.polarity_scores, full_text))
compound = list(map(lambda x: x["compound"], polarity_scores))
avg_comp = sum(compound)/len(compound)

print(avg_comp)
