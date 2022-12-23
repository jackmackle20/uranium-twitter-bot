import tweepy as tw
import json

def authenticator():
    config = open("config.json", "r")
    config = json.load(config)

    api_key = config["api_key"]
    api_key_secret = config["api_key_secret"]
    access_token = config["access_token"]
    access_token_secret = config["access_token_secret"]
    
    authenticator = tw.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    api = tw.API(authenticator, wait_on_rate_limit=True)
    
    return api