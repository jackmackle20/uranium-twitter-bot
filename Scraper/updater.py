import pull_tweets
import sqlite3
from datetime import datetime

conn = sqlite3.connect("storage/test.db")
cur = conn.cursor()
cur.execute("SELECT created_at FROM tweets ORDER BY created_at DESC LIMIT 1")
most_recent_tweet = cur.fetchall()[0][0]
most_recent_tweet = datetime.strptime(most_recent_tweet, "%Y-%m-%d %H:%M:%S%z")
most_recent_tweet = str(most_recent_tweet.isoformat())

print(most_recent_tweet)


pull_tweets.write_to_db(f"'#uranium' since:{'2022-02-24'} -filter:retweets",
                        "storage/test.db",
                        "append")


pull_tweets.sample("test")

conn.close()

    