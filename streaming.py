from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

token = '915287641037393921-R5t9FHYlx5w6ua9sxKo3Nr8hncxgeHW'
token_secret = 'y9OT27rtwRQwtggiqC9TyGu6vfD2rHKc6lCqXevLPriJf'
consumer_key = 'q4VyFKOT8rdkzAr4cirYOteSM'
consumer_secret = 'XFyIAVcDU8bBJ9F71ZDMBmBfYwio1hlfmhx4MlLf1sjyTzGSqd'

# This is the Twitter api streamer; with help of https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/?completed=/mysql-live-database-example-streaming-data/
class listener(StreamListener):
    def data(self, data):
        try:
            print data
            savefile = open('twitdb.csv', 'a')
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException, e:
            print 'failed', str(e)

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)

twitterStream = Stream(auth, listener())
x = twitterStream.filter(track=["#IWD2018"])
