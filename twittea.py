import tweepy
from twitterkeys import consumer_key, consumer_secret, access_token, access_token_secret
from frikada3 import now

fichero = "Book1.xlsx"
sheet = "Muloko"

enmarcha = True


# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
media = api.media_upload(filename="/mnt/c/Users/acont/Documents/Blockstream/BMN/Energía/chart"+now+".png")
texts = []
tweets = []
text = " "
vez = 1
while text != "":
    text = input("Tweet número "+ str(vez) + ". Escribe: ")
    if text != "":
        texts.append(text)
    vez += 1

for i in range(len(texts)):
    if i == 0:
        reply = api.update_status(status=texts[i], media_ids= [media.media_id_string],
        auto_populate_reply_metadata=True)
        tweets.append(reply)
    else:
        reply = api.update_status(status=texts[i], media_ids= [media.media_id_string],
        in_reply_to_status_id=tweets[i - 1].id, auto_populate_reply_metadata=True)
        tweets.append(reply)

print("Gracias por usar este servicio tan espectacular")