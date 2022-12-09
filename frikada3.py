from datos import *
import matplotlib.pyplot as plt


desde = input("Dime desde qué fecha quieres calcular. Formato YYYY-mm-dd. No pongas nada si es BMN: ")

if desde == "":
    print("Es BMN")
    print(tasaCentral, tasaNegativa, tasaPositiva)
    desde = idInicial
    th = 2000
else:
    print("NO ES BMN")
    print(tasaCentral, tasaNegativa, tasaPositiva)
    # desde =

idActual = df2['id'].iloc[-1]
idBMNfinal = desde + (3 * 365)
idTranche1 = 4471
idTranche2 = 4542
idTranche3 = 4634
idTranche4 = 4661
idTranche5 = 4665
idTranche6 = 4667
idTranche7 = 4690
idTranche8 = 4756


def addRows(bmn, ppio, fin, tasa, df2):
    if bmn == "bmnsi":
        bd = 950
        bd2 = bd/2
        tasaLoca = tasa
        tasaC = ((1 + ( tasa       / 100)) ** (1 / 365)) - 1
        tasaP = ((1 + ((tasa + 30) / 100)) ** (1 / 365)) - 1
        tasaN = ((1 + ((tasa - 30) / 100)) ** (1 / 365)) - 1
        print("En este caso la tasa es ", tasaLoca, tasaC, tasaP, tasaN)
        x = 0
        for i in range(ppio, fin):
            if i == ppio:
                bd = 950
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1]+1, 'date': df2.iloc[-1]["date"]+ pd.Timedelta(1, unit='d'),
                                       'NetworkHR': df2.iloc[-1]["NetworkHR"]*(1 + tasaC), 'NetworkHRPos': df2.iloc[-1]["NetworkHR"]*(1 + tasaP),
                                       'NetworkHRNeg': df2.iloc[-1]["NetworkHR"]*(1 + tasaN), 'bitcoins/day': [bd],
                                       'bitcoin_price': df2.iloc[-1]["bitcoin_price"]*(1 + tasaC), 'bitcoin_pricePos': df2.iloc[-1]["bitcoin_price"]*(1 + tasaP),'bitcoin_priceNeg': df2.iloc[-1]["bitcoin_price"]*(1 + tasaN),
                                       'BMN price': df2.iloc[-1]["BMN price"], 'AsicPrice': df2.iloc[-1]["AsicPrice"]})
                df2 = pd.concat([df2, row1], ignore_index=True)
            else:
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1] + 1, 'date': df2.iloc[-1]["date"] + pd.Timedelta(1, unit='d'),
                                     'NetworkHR': df2.iloc[-1]["NetworkHR"] * (1 + tasaC),'NetworkHRPos': df2.iloc[-1]["NetworkHRPos"] * (1 + tasaP),
                                     'NetworkHRNeg': df2.iloc[-1]["NetworkHRNeg"] * (1 + tasaN), 'bitcoins/day': [bd],
                                     'bitcoin_price': df2.iloc[-1]["bitcoin_price"] * (1 + tasaC),'bitcoin_pricePos': df2.iloc[-1]["bitcoin_pricePos"]*(1 + tasaP),'bitcoin_priceNeg': df2.iloc[-1]["bitcoin_priceNeg"]*(1 + tasaN),
                                     'BMN price': df2.iloc[-1]["BMN price"],'AsicPrice': df2.iloc[-1]["AsicPrice"]})
                df2 = pd.concat([df2, row1], ignore_index=True)
    return df2

df3 = addRows('bmnsi', desde, idBMNfinal, tasaCentral, df2)
def addMoreRows(df3):
    df3['bitcoins/day'].loc[idHalving2024 + idActual:] = 475
    df3['mined'] = 1/(df3['NetworkHR'][idInicial:idBMNfinal])
    df3['mined'] =df3['mined'] * 2000 * df3['bitcoins/day']
    df3['minedP'] = 1 / (df3['NetworkHRPos'][idInicial:idBMNfinal])
    df3['minedP'] = df3['minedP'] * 2000 * df3['bitcoins/day']
    df3['minedN'] = 1 / (df3['NetworkHRNeg'][idInicial:idBMNfinal])
    df3['minedN'] = df3['minedN'] * 2000 * df3['bitcoins/day']
    df3['accMined'] = df3['mined'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMinedP'] = df3['accMined'].iloc[idActual] + df3['minedP'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMinedN'] = df3['accMined'].iloc[idActual] + df3['minedN'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['buy1']= preciosTrancheBTC[0]
    df3['buy2']= preciosTrancheBTC[1]
    df3['buy3']= preciosTrancheBTC[2]
    df3['buy4']= preciosTrancheBTC[3]
    df3['buy5']= preciosTrancheBTC[4]
    df3['buy6']= preciosTrancheBTC[5]
    df3['buy7']= preciosTrancheBTC[6]
    df3['buy8']= preciosTrancheBTC[7]
    # df3['buy1USD'] = df3['bitcoin_price'][idTranche1:].multiply(preciosTrancheUSDenBTC[0])
    # df3['buy2USD'] = df3['bitcoin_price'][idTranche2:].multiply(preciosTrancheUSDenBTC[1])
    # df3['buy3USD'] = df3['bitcoin_price'][idTranche3:].multiply(preciosTrancheUSDenBTC[2])
    # df3['buy4USD'] = df3['bitcoin_price'][idTranche4:].multiply(preciosTrancheUSDenBTC[3])
    # df3['buy5USD'] = df3['bitcoin_price'][idTranche5:].multiply(preciosTrancheUSDenBTC[4])
    # df3['buy6USD'] = df3['bitcoin_price'][idTranche6:].multiply(preciosTrancheUSDenBTC[5])
    # df3['buy7USD'] = df3['bitcoin_price'][idTranche7:].multiply(preciosTrancheUSDenBTC[6])
    # df3['buy8USD'] = df3['bitcoin_price'][idTranche8:].multiply(preciosTrancheUSDenBTC[7])
    df3['buy1USD'] = 200000
    df3['buy2USD'] = 200000 # df3['bitcoin_price'][idTranche2:].multiply(preciosTrancheUSDenBTC[1])
    df3['buy3USD'] = 240000 # df3['bitcoin_price'][idTranche3:].multiply(preciosTrancheUSDenBTC[2])
    df3['buy4USD'] = 250000 # df3['bitcoin_price'][idTranche4:].multiply(preciosTrancheUSDenBTC[3])
    df3['buy5USD'] = 260000 # df3['bitcoin_price'][idTranche5:].multiply(preciosTrancheUSDenBTC[4])
    df3['buy6USD'] = 290000 # df3['bitcoin_price'][idTranche6:].multiply(preciosTrancheUSDenBTC[5])
    df3['buy7USD'] = 320000 # df3['bitcoin_price'][idTranche7:].multiply(preciosTrancheUSDenBTC[6])
    df3['buy8USD'] = 270000 # df3['bitcoin_price'][idTranche8:].multiply(preciosTrancheUSDenBTC[7])
    return df3

df4 = addMoreRows(df3)

# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][idHalving2024 + idActual -10:idHalving2024 + idActual +10])
# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][idBMNfinal - 10:idBMNfinal+3])
# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][-10:])
# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][idActual - 10:idActual+40])
# print(df4[['id', 'date', 'bitcoin_price', 'accMined', 'buy1USD']][4530:4570])
def chartIt(idBMNfinal):
    x1 = df4['date'][idInicial:idActual]
    x2 = df4['date'][idActual:idBMNfinal]
    x3 = df4['date'][idBMNInicial:idActual]
    actuals, forecast = x1 <= now, x1 > now
    y1 = df4['buy1'][idInicial:idActual]
    y12 = df4['buy1'][idActual:idBMNfinal]
    y13 = df4['buy4'][idInicial:idActual]
    y14 = df4['buy4'][idActual:idBMNfinal]
    y15 = df4['buy5'][idInicial:idActual]
    y16 = df4['buy5'][idActual:idBMNfinal]
    y17 = df4['buy6'][idInicial:idActual]
    y18 = df4['buy6'][idActual:idBMNfinal]
    y2 = df4['accMined'][idInicial:idActual]
    y22 = df4['accMined'][idActual:idBMNfinal]
    y3 = df4['accMinedP'][idActual:idBMNfinal]
    y4 = df4['accMinedN'][idActual:idBMNfinal]
    y5 = df4['BMN price'][idBMNInicial:idActual]
    plt.figure(figsize=(11, 8))
    plt.plot(x1, y1, '-', label='BTC/BMN price of Tranche 1')
    plt.plot(x2, y12, '--')
    plt.plot(x1, y13, '-', label='BTC/BMN price of Tranche 4')
    plt.plot(x2, y14, '--')
    plt.plot(x1, y15, '-', label='BTC/BMN price of Tranche 5')
    plt.plot(x2, y16, '--')
    plt.plot(x1, y17, '-', label='BTC/BMN price of Tranche 6')
    plt.plot(x2, y18, '--')
    plt.plot(x1, y2, '-', label='Cumulative BTC')
    plt.plot(x2, y22, '--', label='Cumulative BTC Forecast '+str(tasaCentral)+'% hashrate increase')
    plt.plot(x2, y3, '--', label='Cumulative BTC Forecast '+str(tasaPositiva)+'% hashrate increase')
    plt.plot(x2, y4, '--', label='Cumulative BTC Forecast '+str(tasaNegativa)+'% hashrate increase')
    plt.plot(x3, y5, '-', label='BMN/BTC price in SideSwap')
    plt.xlabel('days running')
    plt.ylabel('BTC')
    plt.title('Mine vs Buy for BMN in BTC, date '+now)
    plt.legend()
    plt.savefig('chart' + now + '.png')
    plt.show()
    plt.close('all')

def chartIt2(idBMNfinal):
    x1 = df4['date'][idInicial:idActual]
    x2 = df4['date'][idActual:idBMNfinal]
    x3 = df4['date'][idBMNInicial:idActual]
    # actuals, forecast = x1 <= now, x1 > now
    y1 = df4['buy1USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 1
    y12 = df4['buy1USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 1 forecast
    y13 = df4['buy4USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 4
    y14 = df4['buy4USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 4 forecast
    y15 = df4['buy5USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 5
    y16 = df4['buy5USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 5 forecast
    y17 = df4['buy6USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 6
    y18 = df4['buy6USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 6 forecast
    y2 = df4['accMined'][idInicial:idActual] * df4['bitcoin_price'][idInicial:idActual]
    y22 = df4['accMined'][idActual:idBMNfinal] * df4['bitcoin_price'][idActual:idBMNfinal]
    y3 = df4['accMinedP'][idActual:idBMNfinal] * df4['bitcoin_pricePos'][idActual:idBMNfinal]
    y4 = df4['accMinedN'][idActual:idBMNfinal] * df4['bitcoin_priceNeg'][idActual:idBMNfinal]
    y5 = df4['BMN price'][idBMNInicial:idActual] * df4['bitcoin_price'][idBMNInicial:idActual]
    plt.figure(figsize=(11, 8))
    plt.plot(x1, y1, '-', label='USD price of Tranche 1')
    plt.plot(x2, y12, '--')
    # plt.plot(x1, y13, '-', label='USD price of Tranche 4')
    # plt.plot(x2, y14, '--')
    # plt.plot(x1, y15, '-', label='USD price of Tranche 5')
    # plt.plot(x2, y16, '--')
    # plt.plot(x1, y17, '-', label='USD price of Tranche 6')
    # plt.plot(x2, y18, '--')
    plt.plot(x1, y2, '-', label='Cumulative USD value of mined BTC')
    plt.plot(x2, y22, '--', label='Cumulative USD Forecast '+str(tasaCentral)+'% price&hashrate increases')
    plt.plot(x2, y3, '--', label='Cumulative USD Forecast '+str(tasaPositiva)+'% price&hashrate increases')
    plt.plot(x2, y4, '--', label='Cumulative USD Forecast '+str(tasaNegativa)+'% price&hashrate increases')
    plt.plot(x3, y5, '-', label='BMNUSD price in SideSwap')
    plt.xlabel('days running')
    plt.ylabel('USD')
    plt.title('Mine vs Buy for BMN in USD, date '+now)
    plt.legend()
    plt.savefig('chartUSD' + now + '.png')
    plt.show()
    plt.close('all')
    df4.to_json('dataFrame'+now+'.json')

chartIt(idBMNfinal)
chartIt2(idBMNfinal)
print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoin_price', 'bitcoin_pricePos', 'bitcoin_priceNeg']])
# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoin_price', 'bitcoin_pricePos', 'bitcoin_priceNeg']][idActual])
# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoin_price', 'bitcoin_pricePos', 'bitcoin_priceNeg']][idBMNInicial + 730])
# print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoin_price', 'bitcoin_pricePos', 'bitcoin_priceNeg']][idBMNfinal])
