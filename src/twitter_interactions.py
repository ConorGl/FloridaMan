# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import tweepy

#from set_environment import set_environment

os.getenv('consumer_key')

auth = tweepy.OAuthHandler(os.getenv('consumer_key') , consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)