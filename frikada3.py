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
                                       'bitcoin_price': df2.iloc[-1]["bitcoin_price"]*(1 + tasaC), 'BMN price': df2.iloc[-1]["BMN price"],
                                       'AsicPrice': df2.iloc[-1]["AsicPrice"]})
                df2 = pd.concat([df2, row1], ignore_index=True)
            else:
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1] + 1, 'date': df2.iloc[-1]["date"] + pd.Timedelta(1, unit='d'),
                                     'NetworkHR': df2.iloc[-1]["NetworkHR"] * (1 + tasaC),'NetworkHRPos': df2.iloc[-1]["NetworkHRPos"] * (1 + tasaP),
                                     'NetworkHRNeg': df2.iloc[-1]["NetworkHRNeg"] * (1 + tasaN), 'bitcoins/day': [bd],
                                     'bitcoin_price': df2.iloc[-1]["bitcoin_price"] * (1 + tasaC),'BMN price': df2.iloc[-1]["BMN price"],
                                     'AsicPrice': df2.iloc[-1]["AsicPrice"]})
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
    df3['buy1USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[0])
    df3['buy2USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[1])
    df3['buy3USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[2])
    df3['buy4USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[3])
    df3['buy5USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[4])
    df3['buy6USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[5])
    df3['buy7USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[6])
    df3['buy8USD'] = df3['bitcoin_price'].multiply(preciosTrancheUSDenBTC[7])
    return df3

df4 = addMoreRows(df3)

print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][idHalving2024 + idActual -10:idHalving2024 + idActual +10])
print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][idBMNfinal - 10:idBMNfinal+3])
print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][-10:])
print(df4[['id', 'date', 'NetworkHR', 'NetworkHRPos', 'NetworkHRNeg', 'bitcoins/day', 'bitcoin_price', 'mined', 'minedP', 'minedN', 'accMined', 'accMinedP', 'accMinedN']][idActual - 10:idActual+40])

def chartIt(idBMNfinal):
    x1 = df4['date'][idInicial:idActual]
    x2 = df4['date'][idActual:idBMNfinal]
    x3 = df4['date'][idBMNInicial:idActual]
    actuals, forecast = x1 <= now, x1 > now
    y1 = df4['buy1'][idInicial:idActual]
    y12 = df4['buy1'][idActual:idBMNfinal]
    y2 = df4['accMined'][idInicial:idActual]
    y22 = df4['accMined'][idActual:idBMNfinal]
    y3 = df4['accMinedP'][idActual:idBMNfinal]
    y4 = df4['accMinedN'][idActual:idBMNfinal]
    y5 = df4['BMN price'][idBMNInicial:idActual]
    plt.plot(x1, y1, '-', label='BTC/BMN price of Tranche 1')
    plt.plot(x2, y12, '--')
    plt.plot(x1, y2, '-', label='Cumulative BTC')
    plt.plot(x2, y22, '--', label='Cumulative BTC Forecast '+str(tasaCentral)+'% hashrate increase')
    plt.plot(x2, y3, '--', label='Cumulative BTC Forecast '+str(tasaPositiva)+'% hashrate increase')
    plt.plot(x2, y4, '--', label='Cumulative BTC Forecast '+str(tasaNegativa)+'% hashrate increase')
    plt.plot(x3, y5, '-', label='BMN/BTC price in SideSwap')
    plt.xlabel('days running')
    plt.ylabel('BTC')
    plt.title('Mine vs Buy for BMN in BTC')
    plt.legend()
    plt.savefig('chart' + now + '.png')
    plt.show()
    plt.close('all')

def chartIt2(idBMNfinal):
    x1 = df4['date'][idInicial:idActual]
    x2 = df4['date'][idActual:idBMNfinal]
    x3 = df4['date'][idBMNInicial:idActual]
    actuals, forecast = x1 <= now, x1 > now
    y1 = df4['buy1USD'][idInicial:idActual]
    y12 = df4['buy1USD'][idActual:idBMNfinal]
    y2 = df4['accMined'][idInicial:idActual] * df4['bitcoin_price'][idInicial:idActual]
    y22 = df4['accMined'][idActual:idBMNfinal] * df4['bitcoin_price'][idActual:idBMNfinal]
    y3 = df4['accMinedP'][idActual:idBMNfinal] * df4['bitcoin_price'][idActual:idBMNfinal]
    y4 = df4['accMinedN'][idActual:idBMNfinal] * df4['bitcoin_price'][idActual:idBMNfinal]
    y5 = df4['BMN price'][idBMNInicial:idActual] * df4['bitcoin_price'][idActual:idBMNfinal]
    plt.plot(x1, y1, '-', label='BMN/USD price of Tranche 1')
    plt.plot(x2, y12, '--')
    plt.plot(x1, y2, '-', label='Cumulative USD')
    plt.plot(x2, y22, '--', label='Cumulative USD Forecast '+str(tasaCentral)+'% price&hashrate increases')
    plt.plot(x2, y3, '--', label='Cumulative USD Forecast '+str(tasaPositiva)+'% price&hashrate increases')
    plt.plot(x2, y4, '--', label='Cumulative USD Forecast '+str(tasaNegativa)+'% price&hashrate increases')
    plt.plot(x3, y5, '-', label='BMNUSD price in SideSwap')
    plt.xlabel('days running')
    plt.ylabel('USD')
    plt.title('Mine vs Buy for BMN in USD')
    plt.legend()
    plt.savefig('chartUSD' + now + '.png')
    plt.show()
    plt.close('all')

chartIt(idBMNfinal)
chartIt2(idBMNfinal)
