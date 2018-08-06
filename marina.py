import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'HwJyyIT74SwGsGZQiuX8IS5NG'
consumer_secret = 'n5mxMTKeF7XcDHM5c6xcE7kaoaHL4cRAzQp9oyfzdggVPDn9Kq'
access_token = '1021852203588505601-USEvjD63BvXPsWWnUaBBBr0Kg5EkIE'
access_secret = 'QZsvmFByC68yGSdUNKNwFRt8ofQQ5Oe2ugIoMOKJQV63y'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('marina.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['marina', 'marina silva'])
