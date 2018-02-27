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

    comment_sentiment = blob.sentiment.polarity  # Looks like this line does literally all the work, how does it work?
    
    #https://textblob.readthedocs.io/en/latest/quickstart.html#quickstart this is good explanation

    sentiment_value += comment_sentiment

    num_comments += 1

print('/r/' + "BIZ")
try:  # I wonder if try catch is better to use than "if num_comments > 0" 
    # we can time it some time
    print('Ratio:' + str(math.floor(sentiment_value/num_comments*100)) + "\n")
except:
    print("No comment sentiment." + "\n")
