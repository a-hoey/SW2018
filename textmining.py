import json
import csv
from collections import defaultdict, Counter
from pprint import pprint
import sys

file_name = 'twitdb'
tweets_data_path = ''+file_name+'.csv'
tweets_data = []
tweets_file = open(tweets_data_path, 'r')

def get_hashtags(tweet):
    tweet_entities = tweet.get('entities', None)
    hashtags = tweet_entities.get('hashtags', None)
    return [tag['text'].lower() for tag in hashtags]

def get_text(tweet):
    text_tweet = tweet.get('text', None)
    return [tweet1['text'].lower() for tweet1 in tweet]

if __name__ == '__main__':
    if len(sys.argv) != 1:
        sys.exit(0)
    fname = sys.argv[0]
    with open(fname, 'r') as f:
        hashtag_count = defaultdict(int)
        hashtags = Counter()
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                hashtags_in_tweet = get_hashtags(tweet)
                tweets_data.append(hashtags_in_tweet)

                n_of_hashtags = len(hashtags_in_tweet)
                hashtag_count[n_of_hashtags] += 1
                hashtags.update(hashtags_in_tweet)
                x = hashtags.most_common(30)
                print x
                tweets_with_hashtags = sum([count for n_of_tags, count in hashtag_count.items() if n_of_tags > 0])
                tweets_with_no_hashtags = hashtag_count[0]
                tweets_total = tweets_with_hashtags + tweets_with_no_hashtags

                for tag_count, tweet_count in hashtag_count.items():
                    if tag_count > 0:
                        percent_total = "%.2f" % (tweet_count * 100 / tweets_total * 100)
                        # print("{}tweets with {} hashtags ({}%total)".format(tweet_count, tag_count, percent_total))
            except Exception, err:
                if line != "\n":
                    print(err)
                    print('Error', line)
                    continue

    with open('hashtags1.csv', "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in tweet:
            writer.writerow(tweets_data)


