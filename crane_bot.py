import tweepy
from words import biomes, bitters, creatures, hearts, nakeds, pronouns, squattings
import random 
import os
from os.path import join, dirname
from dotenv import Dotenv

# Twitter Config

try:
    dotenv_path = join(dirname(__file__), '.env')
    dotenv = Dotenv(dotenv_path)
    os.environ.update(dotenv)
except:
    pass

CONSUMER_KEY = os.environ.get("CONSUMER_KEY") 
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)

# In the Desert
desert = random.choice(biomes.biomes)
creature = random.choice(creatures.creatures)
naked = random.choice(nakeds.nakeds) 
squatting = random.choice(squattings.squattings)
heart = random.choice(hearts.hearts)
bitter = random.choice(bitters.bitters)
pronoun = random.choice(pronouns.pronouns)

first_stanza = \
"In the %s\n" % desert + \
"I saw a %s, %s, beastial\n" % (creature, naked) + \
"Who, %s on the ground\n" % squatting + \
"Held %s %s in %s hands\n" % (pronoun[1], heart, pronoun[1]) + \
"And ate of it.\n" 

second_stanza = \
"I said, \"Is it good, friend?\"\n" + \
"It is %s - %s, %s answered;\n" % (bitter, bitter, pronoun[0]) + \
"But I like it\n" + \
"Because it is %s\n" % bitter + \
"And because it is my %s\n" % heart

# Tweet it
if (len(first_stanza) < 140) and (len(second_stanza) < 140):
    first_tweet = api.update_status(first_stanza)
    second_tweet = api.update_status(second_stanza, in_reply_to_status_id = first_tweet.id)
else:
    print "That one was too long"
