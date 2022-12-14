import tweepy
# import json
# import pandas as pd
from datetime import datetime, timedelta
from twitterkeys import consumer_key, consumer_secret, access_token, access_token_secret
from frikada3 import *

def twittealo(idMencion):
    reply = api.update_status(status="Thanks for your interest, here is your chart, showing the expected value of 1 BMN in the remaining period, assuming a "+str(tasaQuestionPrice)+"% annual price increase and "+str(tasaQuestionHR)+"% annual hashrate increase", media_ids=[media4.media_id_string],
                              in_reply_to_status_id=idMencion, auto_populate_reply_metadata=True)
def chartIt3(idBMNfinal):
    x1 = df45['date'][idInicial:idActual]
    x2 = df45['date'][idActual:idBMNfinal]
    x3 = df45['date'][idBMNInicial:idActual]
    y1 = df45['buy1USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 1
    y12 = df45['buy1USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 1 forecast
    y13 = df45['buy4USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 4
    y14 = df45['buy4USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 4 forecast
    y15 = df45['buy5USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 5
    y16 = df45['buy5USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 5 forecast
    y17 = df45['buy6USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 6
    y18 = df45['buy6USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 6 forecast
    y2 = df45['accMined'][idInicial:idActual] * df45['bitcoin_price'][idInicial:idActual]
    y22 = df45['accMined'][idActual:idBMNfinal] * df45['bitcoin_price'][idActual:idBMNfinal]
    y5 = df45['BMN price'][idBMNInicial:idActual] * df45['bitcoin_price'][idBMNInicial:idActual]
    plt.figure(figsize=(11, 8))
    plt.plot(x1, y1, '-', label='USD price of Tranche 1')
    plt.plot(x2, y12, '--')
    plt.plot(x1, y2, '-', label='Cumulative USD value of mined BTC')
    plt.plot(x2, y22, '--', label='Cumulative USD Forecast '+str(tasaQuestionHR)+'% hr&'+str(tasaQuestionPrice)+'price increases')
    plt.plot(x3, y5, '-', label='BMNUSD price in SideSwap')
    plt.xlabel('days running')
    plt.ylabel('USD')
    plt.title('Mine vs Buy for BMN in USD, date '+now)
    plt.legend()
    plt.savefig('chartUSDCustom' + now + '.png')
    plt.close('all')

dfStatuses = pd.read_excel('Statuses.xlsx')
print("dfStatuses es: ", dfStatuses)
tasaQuestionHR = " "
tasaQuestionPrice = " "

d = datetime.today() - timedelta(days=0)
now = str(d.strftime('%d-%m-%Y'))
print(now)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
statuses = api.mentions_timeline(tweet_mode = "extended")

media = api.media_upload(filename="/mnt/c/Users/acont/Documents/Blockstream/BMN/Energía/chart"+now+".png")
media2 = api.media_upload(filename="/mnt/c/Users/acont/Documents/Blockstream/BMN/Energía/chartUSD"+now+".png")
media3 = api.media_upload(filename="/mnt/c/Users/acont/Documents/Blockstream/BMN/Energía/mytable"+now+".png")
# media4 = api.media_upload(filename="chartUSDCustom"+now+".png")

tweets = []

for i in range(len(dfStatuses['Statuses'])):
    tweets.append(int(dfStatuses['Statuses'][i]))

for i in range(len(statuses)):
    # print(type(statuses[i].id), dfStatuses['Statuses'], type(dfStatuses['Statuses']))
    if len(statuses) == 0:
        print("nadie ha interactuado contigo todavía, sorry ")

    elif statuses[i].id not in tweets:
        texto = statuses[i].full_text.split()
        tasaQuestionHR = int(texto[1])
        print("La tasa de HR es: ", tasaQuestionHR)
        tasaQuestionPrice = int(texto[2])
        print("La tasa Precio es: ", tasaQuestionPrice)
        tasaQuestionHRdiaria = ((1 + (tasaQuestionHR / 100)) ** (1 / 365)) - 1
        tasaQuestionPricediaria = ((1 + (tasaQuestionPrice / 100)) ** (1 / 365)) - 1
        print(statuses[i].id, statuses[i].full_text)
        fechaCorregida = statuses[i].created_at
        row = pd.DataFrame({'cuenta': statuses[i].author.name, 'date': str(fechaCorregida),
                             'Statuses': str(statuses[i].id)}, index=[0])
        dfStatuses = pd.concat([dfStatuses, row], ignore_index=True)
        dfStatuses.to_excel(r'Statuses.xlsx', index=False)
        df35 = addRowsCustom('bmnsi', idActual, idBMNfinal, tasaQuestionHRdiaria, tasaQuestionPricediaria, df2)
        df45 = addMoreRowsCustom(df35)
        chartIt3(idBMNfinal)
        media4 = api.media_upload(filename="chartUSDCustom" + now + ".png")
        twittealo(statuses[i].id)

print("Gracias por usar este servicio tan espectacular")