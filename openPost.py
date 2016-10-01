import praw
import webbrowser
from random import randrange
import twilioClient


def openPost(subreddit, numPosts):
    r = praw.Reddit(user_agent='myapp')
    submissions = r.get_subreddit(subreddit).get_hot(limit=numPosts)
    num = randrange(0, numPosts)
    print "Post Number - " + str(num)

    i = 0
    for x in submissions:
        if i == num:
            # webbrowser.open_new_tab(x.url)
            twilioClient.sendMMS(x.url)
            break
        else:
            i = i + 1
