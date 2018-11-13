import tweepy
import csv
import pandas as pd
import os
import apiConfig
api=apiConfig.get_config()
global searchItem
searchItem='unity'
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
    
    
def parseUserDetails(text):
    result=[]
    text=text.split(' ')
    for t in text:
        try:
            if(t[0]=='@'):
                result.append(t)
            else:
                pass
        except:
            return result
    return result
def parseLinkDetails(text):
    result=[]
    text=text.split(' ')
    for t in text:
        try:
            if(re.match('^https',text)):
                result.append(t)
            else:
                pass

        except:
            pass
    return result
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

for tweet in tweepy.Cursor(api.search,q=searchItem,count=100,lang="en",since="2018-11-11").items():
    print (tweet.created_at, tweet.text)
    parseHashTags=parseTextHashtags(tweet.text.encode('utf-8'))
    parseUser=parseUserDetails(tweet.text.encode('utf-8'))
    parseLink=parseLinkDetails(tweet.text.encode('utf-8'))
    
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),parseHashTags,parseUser,parseLink] )

    ##print tweet.text.encode('utf-8')

for key in hashtags.keys():
    csvHashtagWriter.writerow([key,hashtags[key]])