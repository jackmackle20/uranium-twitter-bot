import pull_tweets
import sqlite3
from datetime import date
import os
import pandas as pd
import logging

def update_database():
    today = date.today()

    pull_tweets.write_to_db(f"'#uranium' since:2022-03-01 -filter:retweets",
                            "storage/storage.db",
                            "storage.db",
                            "append")

def run_logger():
    log = pull_tweets.return_log()
    
    log_path = os.path.dirname(os.path.realpath("logs"))
    log_filename = os.path.join(log_path, "logs/pull_tweets.log")
        
    logger = logging.getLogger("updater_test")
    logger.setLevel(logging.DEBUG)

    ch = logging.FileHandler(filename=log_filename)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    
    logger.info(f"entries added: {log['entries_added']}")
    logger.info(f"duplicates removed: {log['duplicates_removed']}")
    
if __name__ == "__main__":
    update_database()
    run_logger()
    
    
    