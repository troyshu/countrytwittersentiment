from TwitterSearch import *


class TwitterSearcher:
  
  def __init__(self):
    try:
        self.tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        self.tso.setKeywords(['Ukraine']) # let's define all words we would like to have a look for
        self.tso.setLanguage('en') # we want to see German tweets only
        self.tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
        self.tso.setIncludeEntities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        self.ts = TwitterSearch(
            consumer_key = 'ZewlOk302H9ydKF0KGcLJQGz8',
            consumer_secret = 'pGBybPshs2G1ncC6S3cYkAF5N2M2lG4x5uh7LHHt4yjdDTsClO',
            access_token = '12981092-z3ZP0PlQj42h9tZk2UUdtDmUqh5iNZsC9uQWfkOah',
            access_token_secret = 'd5wjPYGvFTAsTGGwekcKpQCXi8uthmzdkI77CPEm2e3MW'
         )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

  def search(self, keyword, maxCount = 1000):
    tweets = []
    count = 0
    try:
      self.tso.setKeywords([keyword])
      for tweet in self.ts.searchTweetsIterable(self.tso): # this is where the fun actually starts :)
        if count > maxCount:
          break
        # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        tweets.append(tweet)
        count += 1
    except TwitterSearchException as e:
      print(e)
      
    return tweets