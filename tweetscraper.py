
import re
from  textblob import TextBlob
from datetime import date
import GetOldTweets3 as got
end_date=date.today()
end=end_date.strftime("%Y-%m-%d")

# def clean_tweet(tweet):
#     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
# def get_tweet_sentiment(tweet):
#     analysis= TextBlob(clean_tweet(tweet))
#     if analysis.sentiment.polarity>0:
#         return "positive"
#     elif analysis.sentiment.polarity ==0:
#         return "neutral"
#     else:
# #         return "negative"
def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#21daylockdown')\
                                           .setSince("2020-3-20")\
                                           .setUntil(end)\
                                           .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets=[[tweet.text] for tweet in tweets]
    # for tweets in text_tweets:
    #     print(clean_tweet(tweets))
    # print(clean_tweet(text_tweets))
    return text_tweets
text =""
txt_tweets=get_tweets()
for i in range (0,100):
    text = txt_tweets[i][0]+" "+text
    
print(text)