import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
import csv
from matplotlib import *
import matplotlib.pyplot as plt

file_name = 'twitdb'
tweets_data_path = ''+file_name+'.csv'
tweets_data = []
tweets_file = open(tweets_data_path, 'r')

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

if __name__ == '__main__':
    fname = sys.argv[0]
    tweet_tokenizer = RegexpTokenizer(r'\w+')
    punct = list(string.punctuation)
    stopword_list = stopwords.words('english') + punct + ['rt', 'via', 'https','amp','re','co']

    tf = Counter()
    with open(fname, 'r') as f:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tokens = process(text=tweet['text'],
                                 tokenizer=tweet_tokenizer,
                                 stopwords=stopword_list)

                tf.update(tokens)
                print tf.most_common(30)

                # for tag, count in tf.most_common(20):
                #     print("{}: {}".format(tag, count))

                # plt.barh(range(len(most_common)), [val[1] for val in most_common], align='center')
                # plt.yticks(range(len(most_common)), [val[0] for val in most_common])
                # plt.show()

            except Exception, err:
                if line != "\n":
                    print(err)
                    print('Error', line)
                    continue




