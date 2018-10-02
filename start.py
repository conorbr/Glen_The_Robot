import tweepy
import time
from tweepy.streaming import StreamListener

consumer_key = '0vAK05WbEgGQm5E1OFE5a4iBt'
consumer_secret = 't2dwnFP33vxc2oGdTvXHkrRXJl6RwqUjvRUDdGADu8ABZ4Jf5I'
access_token = '1036224298145472512-eQUYbe8jnCMdO7KBwSIB66wpp4fC7j'
access_token_secret = 'TFJl8i64fWjkLZC75F6qIijldbbrIPQseSXiUwHZYh1cz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

def start_command(tweet):
    if "megan" in tweet():
        # execute system command
    elif "twitter" in tweet():
        # execute system command
    elif "instagram" in tweet():
        # execute system command

def stop_command(tweet):
    if "megan" in tweet():
        reply = ["@TwittaBreen yes master, I started the megan command. Timestamp {time.now}"]
        api.update_status(reply)
        os.execute("python Dexter/GrovePi/Software/Python/grove_led_blink.py")
    elif "twitter" in tweet():
        reply = ["@TwittaBreen yes master, I started the twitter command. Timestamp {time.now}"]
        api.update_status(reply)
        os.execute("python Dexter/GrovePi/Software/Python/grove_led_blink.py")

    elif "instagram" in tweet():
        reply = ["@TwittaBreen yes master, I started the instagram command. Timestamp {time.now}"]
        api.update_status(reply)
        python /Dexter/GrovePi/Software/Python/grove_led_blink.py
        os.execute("python Dexter/GrovePi/Software/Python/grove_led_blink.py")

def tell(tweet)
    reply = ["{handle} oh I'll feckin tell him", "{handle} I'll let him know", "{handle} oh i'll tell him", "don't worry {handle}, he'll hear the words of the irish people"]
    print("new tweet request")
    handle = "@" + mentions.user.screen_name
    response = " " + random.choice(reply).format(handle=handle)
    print("responding to tweet: " + response)
    api.update_status(response, in_reply_to_status_id = mentions.id)
    print("sending trump a tweet...")
    reply = "@realDonaldTrump" + mentions.text.replace("#tellhim", "").replace("#TellHim", "").replace("@Big_Sean_Murph", "")
    api.update_status(reply)
    print(reply)

for mentions in tweepy.Cursor(api.mentions_timeline).items():

    if "start" in mentions.text.lower():
        start_command(mentions.text())
    elif "stop" in mentions.text.lower():

    elif "tell" in mentions.text.lower():

    elif "#stop" in mentions.text.lower():

    elif "#stop" in mentions.text.lower():

    elif "#stop" in mentions.text.lower():
    else:
