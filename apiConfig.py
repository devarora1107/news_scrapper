def get_config():
    import tweepy
    consumer_key = 'fX4iGd2OTOMsP94eEf1yq3KBv'
    consumer_secret = '3dEjoDFPl5cmqgbeyH3wsjEC2MkywgT1IS7RSJC1ZcBFOyBrPo'
    access_token = '1058740982081077253-BwKpwkilxzEJmKKLCtq4nH4VKAhmyJ'
    access_token_secret = 'lI04JwX6YiDF2zxlsuX8T9r7cx6Eg12atvg3XXRbqP4vk'
    searchItem='unity of india'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api