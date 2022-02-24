import json
import sqlite3 
import pandas as pd
import tweepy as tw
import logging

config = "config.json"

logging.basicConfig(filename="logs/pull_tweets.log",
                        format="%(asctime)s %(message)s",
                        encoding="utf-8",
                        level=logging.DEBUG)

def authenticator(config):
    config = open(config, "r")
    config = json.load(config)

    api_key = config["api_key"]
    api_key_secret = config["api_key_secret"]
    access_token = config["access_token"]
    access_token_secret = config["access_token_secret"]
    
    authenticator = tw.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    api = tw.API(authenticator, wait_on_rate_limit=True)
    
    return api

def return_tweet_data(q):
    response = tw.Cursor(authenticator(config).search_tweets,
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
    
    return pd.DataFrame(tweet_data)

#tweet_data = return_tweet_data("'#uranium' since:2022-02-01 -filter:retweets")

def write_to_db(q, db, if_exists):
    conn = sqlite3.connect(db)
    tweet_data = return_tweet_data(q)
    
    #logging.info(f"entries added: {tweet_data.shape[0]}")
    
    tweet_data.to_sql("tweets", 
                      conn,
                      if_exists=if_exists)
    conn.close()

def sample(my_text):
    print(my_text)
    
    



