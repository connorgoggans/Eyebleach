from openPost import openPost
import random
import time

postNum = None
phoneNumber = None


def main():
    subreddits = [
        'eyebleach', 'aww', 'blep', 'blop', 'animalsbeingbros',
        'corgi', 'cats', 'catloaf', 'delightfullychubby', 'dogpictures',
        'tuckedinkitties', 'husky', 'redpandas', 'babygoats', 'babyhippos',
        'babykoala', 'babywildanimals', 'beagle', 'catbellies', 'catpics',
        'catsinboxes', 'catsinsinks', 'chinchilla', 'cute', 'daww',
        'fennecfoxes', 'ferrets', 'foxes', 'goats', 'hamsters', 'hedgehog',
        'jellybeantoes', 'kittens', 'koalas', 'ocelots', 'otters',
        'polarbears', 'puppies', 'rabbits', 'sleepinganimals', 'snowleopards',
        'stuffoncats', 'tuxedocats'
    ]

    choice = random.choice(subreddits)
    print "Subreddit - " + choice
    postNum = 50
    openPost(choice, postNum, phoneNumber)

if __name__ == "__main__":
    postNum = int(raw_input("What number of top posts per sub: "))
    phoneNumber = "+" + raw_input("Phone Number: ")
    while True:
        main()
        time.sleep(2)
