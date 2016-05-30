from twython import Twython
from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
import random
messages = [
    "Hello world",
    "Hi there",
    "What's up",
    "How it's going",
    "where have you been?",
    "Get the bike ride!"
    ]
twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: %s" % message)
