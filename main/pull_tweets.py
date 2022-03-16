import json
import sqlite3 
import pandas as pd
import tweepy as tw
import twitter_api
import os

log = {}

def return_tweet_data(q):
    response = tw.Cursor(twitter_api.authenticator().search_tweets,
                         q=q,
                         lang="en",
                         tweet_mode="extended",
                         count=100)

    tweet_id = []
    created_at = []
    entities = []
    in_reply_to_status = []
    full_text = []
    verified = []
    retweet_count = []
    user_id = []
    user_name = []
    user_followers_count = []


    for tweet in response.items(10000):
        tweet_id.append(tweet.id_str)
        created_at.append(tweet.created_at)
        entities.append(tweet.entities)
        in_reply_to_status.append(tweet.in_reply_to_status_id_str)
        full_text.append(tweet.full_text)
        verified.append(tweet.user.verified)
        retweet_count.append(tweet.retweet_count)
        user_id.append(tweet.user.id_str)
        user_name.append(tweet.user.screen_name)
        user_followers_count.append(tweet.user.followers_count)
        
    tweet_data = {"tweet_id" : tweet_id,
            "created_at" : created_at,
            #"entities" : entities,
            "in_reply_to_status" : in_reply_to_status,
            "full_text" : full_text,
            "verified" : verified,
            "retweet_count" : retweet_count,
            "user_id" : user_id,
            "user_name" : user_name,
            "user_followers_coubt" : user_followers_count}
    
    df = pd.DataFrame(tweet_data)
    
    log["entries_added"] = df.shape[0]

    return df

def write_to_db(q, db_dir, db, if_exists):
    db_path = os.path.dirname(os.path.realpath(db_dir))
    db_filename = os.path.join(db_path, db)
    
    conn = sqlite3.connect(db_filename)
    tweet_data = return_tweet_data(q)
    
    tweet_data.to_sql("tweets", 
                      conn,
                      if_exists=if_exists,
                      index=False)
    
    #check for duplicates
    df = pd.read_sql_query("SELECT * FROM tweets",
                           conn)
    
    init = df.shape[0]
    
    df = df.drop_duplicates(subset=["tweet_id"])
    
    fin = df.shape[0]
    
    log["duplicates_removed"] = init - fin 
    
    df.to_sql("tweets",
              conn,
              if_exists="replace",
              index=False)
    
    conn.close()
    
def return_log():
    return log
    
    



