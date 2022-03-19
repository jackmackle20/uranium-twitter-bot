# Introduction #

Over the past year I have become heavily interested in the emerging Uranium bull market. To stay informed, I pay close attention to uranium Twitter, which is filled with panicky retail investors (myself included), reputable media outlets, and a few uranium market experts with high conviction for this investment thesis. 

I was interested in understanding the general sentiment of the investment community towards uranium, so I came up with this bot. You can check out the bot on Twitter [@u3o8_botman](https://twitter.com/u3o8_botman).

# Description #

### Pulling Tweets ###
I used the tweepy module and Twitter standard API to search for tweets containing #uranium daily. The search query filters out retweets. 

### Storing the Data ###
The data is stored locally in an SQLite database.

### Model ###
I used the [VADER](https://github.com/cjhutto/vaderSentiment) (Valence Aware Dictionary and sEntiment Reasoner). There are more details on why I chose this model as well as some other analysis [here](https://github.com/jackmackle12/uranium-twitter-bot/blob/master/notebooks/001-Vader.ipynb).

### Deployment ###
I provisioned a basic virtual machine through Digital Ocean and run the bot with a cron job. The operating costs are ~ $3.60/month CAD. 




