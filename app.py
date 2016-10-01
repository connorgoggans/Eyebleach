from openPost import openPost
import random
import time


def main():
    subreddits = [
    'eyebleach', 'aww', 'blep', 'blop', 'animalsbeingbros',
    'corgi', 'cats', 'catloaf', 'catgifs', 'delightfullychubby', 'dogpictures',
    'tuckedinkitties', 'husky', 'redpandas'
    ]

    choice = random.choice(subreddits)
    print "Subreddit - " + choice
    postNum = 10
    openPost(choice, postNum)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
