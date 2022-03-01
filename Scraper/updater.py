import pull_tweets
import sqlite3
from datetime import date

def update_database():
    today = date.today()

    pull_tweets.write_to_db(f"'#uranium' {today} -filter:retweets",
                            "storage/storage.db",
                            "storage.db",
                            "append")

if __name__ == "__main__":
    update_database()
    
    