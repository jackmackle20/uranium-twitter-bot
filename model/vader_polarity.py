import pandas as pd
import numpy as np 
import sqlite3
import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def query_db():
    db_path = os.path.dirname(os.path.realpath("storage/storage.db"))
    db_filename = os.path.join(db_path, "storage.db")
    
    conn = sqlite3.connect(db_filename)
    
    df = pd.read_sql_query("SELECT * FROM tweets", conn)
    
    conn.close()
    
    return df 

def do_vader():
    
    
