import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime
fname = "bolsonaro" + datetime.datetime.now().strftime("%d-%m") + ".json"

consumer_key = 'O6fJRuYJBnB4cqfQPf2stHPTd'
consumer_secret = 'rMS6Hi3IcMyP16QX3Zg15oVmSj1JuR5xcK5SCfqy7xLXmirJ4G'
access_token = '986070861865279488-BPOVGT90tAR1wMiVPGRHLHvLUA547Fb'
access_secret = 'AG73nImEpRylglwUMDoy88x1bsblRTj47XAVQvOJc1px3'

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
twitter_stream.filter(track=['bolsonaro'])
