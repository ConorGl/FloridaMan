# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import tweepy
import csv
from dotenv import load_dotenv
from datetime import datetime
import io


load_dotenv()
#from set_environment import set_environment

class TwitterInteractor:
    #Initialises a basic Twitter Interactor which uses the environment to set
    #the auth credentials. Has a single function which uses those functions to 
    #print a list of tweets from the timeline
    def __init__(self):
        self.auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'] , os.environ['CONSUMER_SECRET'])
        self.auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(self.auth)
    
    def print_home_tweets(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)
            
    def save_query_tweets(self):
        public_tweets = self.api.home_timeline()
        with open('basic_tweets.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tweet.text for tweet in public_tweets)
                
        

twitter = TwitterInteractor()    
twitter.get_basic_tweets()
twitter.save_basic_tweets()

with io.open('basic_tweets.csv','w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    try:
        for tweet in tweepy.Cursor(twitter.api.search, q='Florida Man',lang='en', count=1000).items():        
            tweets_encoded=tweet.text.encode('utf-8')
            tweets_decoded=tweets_encoded.decode('utf-8')
            writer.writerow([datetime.now().strftime("%Y-%m-%d  %H:%M")
                                , tweet.id, tweets_decoded, tweet.created_at, tweet.geo
                                , tweet.place.name if tweet.place else None
                                , tweet.coordinates, tweet._json["user"]["location"]])
    except tweepy.RateLimitError:
        print("Something went wrong, too many calls")
            