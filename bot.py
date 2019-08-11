from PIL import Image, ImageDraw, ImageFont
import random
import time
import tweepy

CONSUMER_KEY = 'xMXlpEDdkxJWpEQEjGpFo2I5O'
CONSUMER_SECRET = 'vk5QWocPxSjGFfHg89kr9kOaA3YGk9AORycgjKsaS0zB2A7jbb'
ACCESS_KEY = '1160436507527843841-nyYlBedWqnJA7xy9ZG6xw824BBTqYU'
ACCESS_SECRET = '9yfrkoQ743J3ascW5DuFkV5bhYu9NINipizTcFblKasSP'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

words = open('wordsing.txt', 'r').readlines()



print("Starting, we is good")




while(True):
    image = Image.open('base.png')
    emoji = Image.open('emoji.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=26)
    (x, y) = (200, 482)
    color = 'rgb(255, 255, 255)' # white color
    message = random.choice(words)
    print(message)
    draw.text((x, y), message, fill=color, font=font)
    newX = 200 + len(message) * 13
    image.paste(emoji, (newX, 482))
    image.paste(emoji, (newX + 35, 482))
    image.paste(emoji, (newX + 70, 482))
    image.save('newBase.png')
    api.update_with_media('newBase.png', 'we ' + message)
    time.sleep(21600)


