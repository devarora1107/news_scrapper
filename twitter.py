import tweepy
import csv
import pandas as pd
import os
import apiConfig
api=apiConfig.get_config()
global searchItem
searchItem='RBI'
####input your credentials here

#####United Airlines
# Open/Create a file to append data
try:
    os.mkdir('data/'+searchItem)
except:
    os.mkdir('data/'+searchItem+' new')
csvFile = open('data/'+searchItem+'/usageHashtag.csv', 'a')
csvHashtag=open('data/'+searchItem+'/hashtag.csv','a')
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

for tweet in tweepy.Cursor(api.search,q=searchItem,count=100,
                           lang="en",
                           since="2018-11-03").items():
    #print (tweet.created_at, tweet.text)
    parseText=parseTextHashtags(tweet.text.encode('utf-8'))
    #print parseText
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),parseText] )



for key in hashtags.keys():
    csvHashtagWriter.writerow([key,hashtags[key]])