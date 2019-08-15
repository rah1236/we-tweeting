from PIL import Image, ImageDraw, ImageFont
import random
import time
import tweepy



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


