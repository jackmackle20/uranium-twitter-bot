import pull_tweets
import sqlite3
from datetime import date, timedelta
import os
import model
import logging
import tweepy as tw 
import twitter_api 

today = date.today() - timedelta(days=1)
tempd_path = os.path.dirname(os.path.realpath("logs"))
tempd_filename = os.path.join(tempd_path, "logs/tempd.txt")

with open(tempd_filename, "w") as t:
    t.write(str(today))
    
def update_database():
    pull_tweets.write_to_db(f"'#uranium' since:{today} -filter:retweets",
                            "storage/storage.db",
                            "storage.db",
                            "append")
    
def make_tweet():
    sid = model.model(today)
    sid = round(sid, 3)
    api = twitter_api.authenticator()
    global payload 
    payload = f"#uranium twitter sentiment ({today}): {sid}"
    api.update_status(payload)

def run_logger():
    log = pull_tweets.return_log()
    
    log_path = os.path.dirname(os.path.realpath("logs"))
    log_filename = os.path.join(log_path, "logs/updater.log")
        
    logger = logging.getLogger("updater")
    logger.setLevel(logging.DEBUG)

    ch = logging.FileHandler(filename=log_filename)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    
    logger.info(f"entries added: {log['entries_added']}")
    logger.info(f"duplicates removed: {log['duplicates_removed']}")
    logger.info(f"today: {today}")
    logger.info(f"payload: {payload}")
    
if __name__ == "__main__":
    update_database()
    make_tweet()
    run_logger()
    