import json
import csv
from collections import defaultdict, Counter
from pprint import pprint
import sys
from argparse import ArgumentParser

file_name = 'twitdb'
tweets_data_path = ''+file_name+'.csv'
tweets_data = []
tweets_file = open(tweets_data_path, 'r')

def get_place(tweet):
    tweet_places = tweet.get("place")
    country = tweet_places.get("country", None)
    return country

if __name__ == '__main__':
    if len(sys.argv) != 1:
        sys.exit(0)
    fname = sys.argv[0]
    with open(fname, 'r') as f:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                for line in tweet:
                    try:
                        location_of_tweet = get_place(tweet)
                        tweets_data.append(location_of_tweet)
                        # places.update(location_of_tweet)
                        # x = places
                        # print location_of_tweet
                    except:
                        continue

                places = Counter(tweets_data)
                print places
                        # tweets_data.append(location_of_tweet)

            except Exception, err:
                if line != "\n":
                    print(err)
                    print('Error', line)
                    exit()

