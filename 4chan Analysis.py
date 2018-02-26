import basc_py4chan
from textblob import TextBlob
import time
import math

board = basc_py4chan.Board('biz')
allthreads = board.get_all_threads()
num_comments = 0
sentiment_value = 0

for thread in allthreads:
    blob = TextBlob(thread.topic.text_comment.lower())

    comment_sentiment = blob.sentiment.polarity

    sentiment_value += comment_sentiment

    num_comments += 1

print('/r/' + "BIZ")
try:
    print('Ratio:' + str(math.floor(sentiment_value/num_comments*100)) + "\n")
except:
    print("No comment sentiment." + "\n")
