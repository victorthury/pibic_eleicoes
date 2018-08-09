import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime
fname = "resto" + datetime.datetime.now().strftime("%d-%m") + ".json"


consumer_key = 'YfETbY1kvwmiuRgmc9NWeKaOu'
consumer_secret = 'nZkgN5U4U26vjUdNNflEpxjb0HTWoS1QNEKdljPWSADcF9VUw2'
access_token = '1022198016256696320-eIvJ5VLsC24zWu3rMY0AHzUbVANtXV'
access_secret = 'uxIVCSwVPKuQMF8xZAnLgMkGEi38ZjntEKxdXLxdOFHvc'

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
twitter_stream.filter(track=['Alvaro Dias', 'Daciolo', 'Ciro Gomes', 'Boulos', 'Henrique Meirelles', 'Meirelles', 'amoedo', 'goulart', 'eymael', 'davila', 'vera lucia'])
