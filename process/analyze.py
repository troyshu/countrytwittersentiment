from process.twitter import TwitterSearcher
from textblob import TextBlob

class SentimentAnalyzer:
  def __init__(self, type="twitter"):
    self.type = type
    if self.type=='twitter':
      self.twitterSearcher = TwitterSearcher()
    else:
      raise Exception('not yet implemented for news type %s' % self.type)
      
  def _getSentiments(self, keyword, count=200):
    if self.type=='twitter':
      tweetObjs = self.twitterSearcher.search(keyword,count)
      texts = [tweetObj['text'] for tweetObj in tweetObjs]
    else:
      raise Exception('not yet implemented for news type %s' % self.type)
    
    sentiments = [TextBlob(text).sentiment for text in texts]
    return sentiments
  
  def calculateAggregateSentiment(sentimentObjs, method='weighted'):
    
    #if method=='weighted':
      # sentiment polarity weighted by subjectivity
    return None  
  