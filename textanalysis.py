import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
import csv
from pprint import *
from os import path
from prettytable import PrettyTable
from matplotlib import *

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
    stopword_list = stopwords.words('english') + punct + ['rt', 'via', 'https','amp','re','...']

    tf = Counter()
    with open(fname, 'r') as f:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tokens = process(text=tweet['text'],
                                 tokenizer=tweet_tokenizer,
                                 stopwords=stopword_list)
                tf.update(tokens)
                most_common = tf.most_common(30)
                # print tokens

                thefile = open('words.txt', 'w')
                for i in tokens:
                    print i
                    thefile.write(i)

                # plt.hist(most_common)
                # plt.show
                # for label, data in tf:
                #     pt = PrettyTable(field_names=[label, 'Count'])
                #     [pt.add_row(kv) for kv in most_common]
                #     pt.align[label], pt.align['Count'] = 'l', 'r'  # Set column alignment
                #     print pt

                # wordcloud = WordCloud().generate(tf)
                # print wordcloud
                #
                # plt.imshow(wordcloud, interpolation='bilinear')
                # plt.axis("off")

                # lower max_font_size
                # wordcloud = WordCloud(max_font_size=40).generate(text)
                # plt.figure()
                # plt.imshow(wordcloud, interpolation="bilinear")
                # plt.axis("off")
                # plt.show()


                # print tf.most_common(30)
                # for tag, count in tf.most_common(20):
                #     print("{}: {}".format(tag, count))


            except Exception, err:
                if line != "\n":
                    print(err)
                    print('Error', line)
                    continue




