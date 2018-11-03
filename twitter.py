import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'fX4iGd2OTOMsP94eEf1yq3KBv'
consumer_secret = '3dEjoDFPl5cmqgbeyH3wsjEC2MkywgT1IS7RSJC1ZcBFOyBrPo'
access_token = '1058740982081077253-BwKpwkilxzEJmKKLCtq4nH4VKAhmyJ'
access_token_secret = 'lI04JwX6YiDF2zxlsuX8T9r7cx6Eg12atvg3XXRbqP4vk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
csvHashtag=open('hashtag.csv','a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvHashtagWriter=csv.writer(csvHashtag)
hashtags={}
def sortHashtag(string):
    global hashtags
    if(string in hashtags.keys()):

        hashtags[string]=hashtags[string]+1
    else:
        hashtags[string]=1
    
    

def parseTextHashtags(text):
    result=[]
    text=text.split(' ')
    for t in text:
        try:
            if(t[0]=='#'):
                result.append(t)
        except:
            pass
    for hashtag in result:
        sortHashtag(hashtag)
    return result

for tweet in tweepy.Cursor(api.search,q="#cbi",count=100,
                           lang="en",
                           since="2018-11-03").items():
    #print (tweet.created_at, tweet.text)
    parseText=parseTextHashtags(tweet.text.encode('utf-8'))
    #print parseText
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),parseText] )



for key in hashtags.keys():
    csvHashtagWriter.writerow([key,hashtags[key]])