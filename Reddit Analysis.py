import praw
from textblob import TextBlob
import math
import time

reddit = praw.Reddit(client_id = 'GEP04PzgZRRwvg',
                     client_secret = 'N-jq0fnw4C9kCP-zOTQTfb_-0Bs',
                     user_agent = 'subSentiment')


def testModule(Subreddit_Name):
    day_start = (time.time()- 10000)
    day_end = time.time()

    subreddit = reddit.subreddit(Subreddit_Name)

    sub_submissions = subreddit.submissions(day_start, day_end)

    sub_sentiment = 0
    num_comments = 0

    for submission in sub_submissions:
        if not submission.stickied:
            submission.comments.replace_more(limit=0)  # Why do we need to remove all MoreComments instances?
            for comment in submission.comments.list():
                blob = TextBlob(comment.body)

                comment_sentiment = blob.sentiment.polarity

                sub_sentiment += comment_sentiment

                num_comments += 1

    print('/r/' + str(subreddit.display_name))
    try:
        print('Ratio:' + str(math.floor(sub_sentiment/num_comments*100)) + "\n")
    except:
        print("No comment sentiment." + "\n")


Subreddit_Name = 'CryptoCurrency'

testModule(Subreddit_Name)