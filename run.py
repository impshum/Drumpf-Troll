import sys
import time
import tweepy
import random
from config import *


class Colour:
    Green, Red, White, Yellow = '\033[92m', '\033[91m', '\033[0m', '\033[93m'


print(Colour.Yellow + """
╔╦╗╦═╗╦ ╦╔╦╗╔═╗╔═╗  ╔╦╗╦═╗╔═╗╦  ╦
 ║║╠╦╝║ ║║║║╠═╝╠╣    ║ ╠╦╝║ ║║  ║
═╩╝╩╚═╚═╝╩ ╩╩  ╚     ╩ ╩╚═╚═╝╩═╝╩═╝
A PIECE OF SCRAP TO TROLL THAT TWAT
""")

mins = timer / 60
print(Colour.White + 'Checking every {}'.format(int(mins)),
      'minutes\n\nPress Ctrl + C to exit\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

d = time.strftime('%a %H:%M:%S')

p2 = 'putln2'

if follow:
    try:
        api.create_friendship(p2)
    except tweepy.TweepError as e:
        print(e, '\n')


def drumpf():
    with open('data/drumpf.txt', 'r') as l:
        latest = l.read()

    g = api.user_timeline(screen_name='realDonaldTrump',
                          count=1, include_rts=False)

    for s in g:
        tweet = s.text
        post = s.id

    twat = random.choice(replies)
    twit = twat, hashtags
    twit = ' '.join(twit)

    try:
        if latest != tweet:
            print(Colour.Green + d, '- Found new tweet:', tweet)
            print(d, '- Replying with:', twit, '\n')
            api.update_status(twit, post)
            with open('data/drumpf.txt', 'w') as f:
                f.write(tweet)
        else:
            print(Colour.Red + d,
                  '- No new bullshit from Drumpf to spam back at. Grr!')

    except tweepy.TweepError as e:
        print(Colour.White + e)
        sys.exit(1)

while True:
    try:
        drumpf()
        time.sleep(timer)
    except KeyboardInterrupt:
        print(Colour.White + '\nExiting\n')
        sys.exit(1)
