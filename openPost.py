import praw
import webbrowser
from random import randrange
import twilioClient


usedLinks = set()


def openPost(subreddit, numPosts, phoneNumber):
    r = praw.Reddit(user_agent='myapp')
    submissions = r.get_subreddit(subreddit).get_hot(limit=numPosts)
    num = randrange(0, numPosts)
    print "Post Number - " + str(num)

    i = 0
    for x in submissions:
        if i == num:
            # webbrowser.open_new_tab(x.url)
            if("youtube" in x.url or "yout.be" in x.url or "gif" in x.url or "comments" in x.url or x.url is None or x.url in usedLinks):
                print "caught invalid - " + x.url
                openPost(subreddit, numPosts)
                return
            twilioClient.sendMMS(x.url, subreddit, phoneNumber)
            usedLinks.add(x.url)
            return
        else:
            i = i + 1
