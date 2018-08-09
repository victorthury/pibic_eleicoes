import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime
fname = "alckmin" + datetime.datetime.now().strftime("%d-%m") + ".json"

consumer_key = '4EQd43EO8zLeeutMYIzyF2kKI'
consumer_secret = '34W5Vh0ZO16dh6dMkFE7gbizWtwmdyQtViW2o4WOIe87DjKOcK'
access_token = '1021876773431271426-qk1R9v9KXubHWjM6xuqVTktuXauz41'
access_secret = 'gs6Pm0pRh2ns6TIIgmL2MHxZBYJbhdDKRwl8F4CgXCBjq'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open(fname, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Alckmin'])
