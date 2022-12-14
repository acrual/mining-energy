from datos import *
import matplotlib.pyplot as plt
import dataframe_image as dfi
from tabulate import tabulate
# from PIL import Image
# import mimetypes
print("__name__ is: ", __name__)
desde = idInicial
th = 2000

tasasHR = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tasasPrice = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tasasDiariasHR = []
tasasDiariasPrice = []
for tasaHR in tasasHR:
    tasasDiariasHR.append(((1 + (tasaHR / 100)) ** (1 / 365)) - 1)
for tasaPrice in tasasPrice:
    tasasDiariasPrice.append(((1 + (tasaPrice / 100)) ** (1 / 365)) - 1)

idActual = df2['id'].iloc[-1]
idBMNfinal = desde + (3 * 365) + 1
print(idActual, idBMNfinal, "estos son idactual y idbmnfinal")
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
        for i in range(ppio, fin):
            if i == ppio:
                bd = 950
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1]+1, 'date': df2.iloc[-1]["date"]+ pd.Timedelta(1, unit='d'),
                                       'NetworkHR': df2.iloc[-1]["NetworkHR"]*(1 + tasaC), 'NetworkHRPos': df2.iloc[-1]["NetworkHR"]*(1 + tasaP),
                                       'NetworkHRNeg': df2.iloc[-1]["NetworkHR"]*(1 + tasaN), 'bitcoins/day': [bd],
                                       'bitcoin_price': df2.iloc[-1]["bitcoin_price"]*(1 + tasaC), 'bitcoin_pricePos': df2.iloc[-1]["bitcoin_price"]*(1 + tasaP),'bitcoin_priceNeg': df2.iloc[-1]["bitcoin_price"]*(1 + tasaN),
                                       'BMN price': df2.iloc[-1]["BMN price"], 'AsicPrice': df2.iloc[-1]["AsicPrice"], 'HR10': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[0]),'HR20': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[1]),
                                     'HR30': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[2]),'HR40': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[3]),
                                     'HR50': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[4]),'HR60': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[5]),
                                     'HR70': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[6]),'HR80': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[7]),
                                     'HR90': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[8]),'HR100': df2['NetworkHR'].iloc[-1] * (1 + tasasDiariasHR[9]),
                                     'bitcoinP10': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[0]),'bitcoinP20': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[1]),
                                     'bitcoinP30': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[2]),'bitcoinP40': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[3]),
                                     'bitcoinP50': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[4]),'bitcoinP60': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[5]),
                                     'bitcoinP70': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[6]),'bitcoinP80': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[7]),
                                     'bitcoinP90': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[8]),'bitcoinP100': df2['bitcoin_price'].iloc[-1] * (1 + tasasDiariasPrice[9])},index=[0])
                df2 = pd.concat([df2, row1], ignore_index=True)
                # df2 = pd.concat([df2, row2], ignore_index=True)
            else:
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1] + 1, 'date': df2.iloc[-1]["date"] + pd.Timedelta(1, unit='d'),
                                     'NetworkHR': df2.iloc[-1]["NetworkHR"] * (1 + tasaC),'NetworkHRPos': df2.iloc[-1]["NetworkHRPos"] * (1 + tasaP),
                                     'NetworkHRNeg': df2.iloc[-1]["NetworkHRNeg"] * (1 + tasaN), 'bitcoins/day': [bd],
                                     'bitcoin_price': df2.iloc[-1]["bitcoin_price"] * (1 + tasaC),'bitcoin_pricePos': df2.iloc[-1]["bitcoin_pricePos"]*(1 + tasaP),'bitcoin_priceNeg': df2.iloc[-1]["bitcoin_priceNeg"]*(1 + tasaN),
                                     'BMN price': df2.iloc[-1]["BMN price"],'AsicPrice': df2.iloc[-1]["AsicPrice"], 'HR10': df2['HR10'].iloc[-1] * (1 + tasasDiariasHR[0]),'HR20': df2['HR20'].iloc[-1] * (1 + tasasDiariasHR[1]),
                                     'HR30': df2['HR30'].iloc[-1] * (1 + tasasDiariasHR[2]),'HR40': df2['HR40'].iloc[-1] * (1 + tasasDiariasHR[3]),
                                     'HR50': df2['HR50'].iloc[-1] * (1 + tasasDiariasHR[4]),'HR60': df2['HR60'].iloc[-1] * (1 + tasasDiariasHR[5]),
                                     'HR70': df2['HR70'].iloc[-1] * (1 + tasasDiariasHR[6]),'HR80': df2['HR80'].iloc[-1] * (1 + tasasDiariasHR[7]),
                                     'HR90': df2['HR90'].iloc[-1] * (1 + tasasDiariasHR[8]),'HR100': df2['HR100'].iloc[-1] * (1 + tasasDiariasHR[9]),
                                     'bitcoinP10': df2['bitcoinP10'].iloc[-1] * (1 + tasasDiariasPrice[0]),'bitcoinP20': df2['bitcoinP20'].iloc[-1] * (1 + tasasDiariasPrice[1]),
                                     'bitcoinP30': df2['bitcoinP30'].iloc[-1] * (1 + tasasDiariasPrice[2]),'bitcoinP40': df2['bitcoinP40'].iloc[-1] * (1 + tasasDiariasPrice[3]),
                                     'bitcoinP50': df2['bitcoinP50'].iloc[-1] * (1 + tasasDiariasPrice[4]),'bitcoinP60': df2['bitcoinP60'].iloc[-1] * (1 + tasasDiariasPrice[5]),
                                     'bitcoinP70': df2['bitcoinP70'].iloc[-1] * (1 + tasasDiariasPrice[6]),'bitcoinP80': df2['bitcoinP80'].iloc[-1] * (1 + tasasDiariasPrice[7]),
                                     'bitcoinP90': df2['bitcoinP90'].iloc[-1] * (1 + tasasDiariasPrice[8]),'bitcoinP100': df2['bitcoinP100'].iloc[-1] * (1 + tasasDiariasPrice[9])},index=[0])
                df2 = pd.concat([df2, row1], ignore_index=True)
                # df2 = pd.concat([df2, row2], ignore_index=True)
    return df2

def addRowsCustom(bmn, ppio, fin, tasaQuestionHR, tasaQuestionPrice, df2):
    if bmn == "bmnsi":
        bd = 950
        # bd2 = bd/2
        for i in range(ppio, fin):
            if i == ppio:
                bd = 950
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1]+1, 'date': df2.iloc[-1]["date"]+ pd.Timedelta(1, unit='d'),
                                       'NetworkHR': df2.iloc[-1]["NetworkHR"]*(1 + tasaQuestionHR), 'bitcoins/day': [bd],
                                       'bitcoin_price': df2.iloc[-1]["bitcoin_price"]*(1 + tasaQuestionPrice),'BMN price': df2.iloc[-1]["BMN price"], 'AsicPrice': df2.iloc[-1]["AsicPrice"]},index=[0])
                df2 = pd.concat([df2, row1], ignore_index=True)
            else:
                row1 = pd.DataFrame({'id': df2['id'].iloc[-1] + 1, 'date': df2.iloc[-1]["date"] + pd.Timedelta(1, unit='d'),
                                     'NetworkHR': df2.iloc[-1]["NetworkHR"] * (1 + tasaQuestionHR),'bitcoins/day': [bd],'bitcoin_price': df2.iloc[-1]["bitcoin_price"] * (1 + tasaQuestionPrice),
                                     'BMN price': df2.iloc[-1]["BMN price"],'AsicPrice': df2.iloc[-1]["AsicPrice"]},index=[0])
                df2 = pd.concat([df2, row1], ignore_index=True)
    return df2

df3 = addRows('bmnsi', idActual, idBMNfinal, tasaCentral, df2)
# tasaQuestionHR = int(input("Dime que tasa anual de HR quieres tener: "))
# tasaQuestionPrice = int(input("Dime que tasa anual de precio quieres tener: "))
# tasaQuestionHR = ((1 + ( tasaQuestionHR       / 100)) ** (1 / 365)) - 1
# tasaQuestionPrice = ((1 + ( tasaQuestionPrice       / 100)) ** (1 / 365)) - 1
# df35 = addRowsCustom('bmnsi', idActual, idBMNfinal, tasaQuestionHR, tasaQuestionPrice, df2)
def addMoreRows(df3):
    df3['bitcoins/day'].loc[idHalving2024 + idActual:] = 475
    df3['mined'] = 1/(df3['NetworkHR'][idInicial:idBMNfinal])
    df3['mined'] =df3['mined'] * 2000 * df3['bitcoins/day']
    # df3['minedP'] = 1 / (df3['NetworkHRPos'][idInicial:idBMNfinal])
    # df3['minedP'] = df3['minedP'] * 2000 * df3['bitcoins/day']
    # df3['minedN'] = 1 / (df3['NetworkHRNeg'][idInicial:idBMNfinal])
    # df3['minedN'] = df3['minedN'] * 2000 * df3['bitcoins/day']
    df3['accMined'] = df3['mined'][idInicial:idBMNfinal].cumsum(axis=0)
    # df3['accMinedP'] = df3['accMined'].iloc[idActual] + df3['minedP'][idInicial:idBMNfinal].cumsum(axis=0)
    # df3['accMinedN'] = df3['accMined'].iloc[idActual] + df3['minedN'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['mined10'] = 1/(df3['HR10'][idInicial:idBMNfinal])
    df3['mined10'] = df3['mined10'] * 2000 * df3['bitcoins/day']
    df3['mined20'] = 1 / (df3['HR20'][idInicial:idBMNfinal])
    df3['mined20'] = df3['mined20'] * 2000 * df3['bitcoins/day']
    df3['mined30'] = 1 / (df3['HR30'][idInicial:idBMNfinal])
    df3['mined30'] = df3['mined30'] * 2000 * df3['bitcoins/day']
    df3['mined40'] = 1 / (df3['HR40'][idInicial:idBMNfinal])
    df3['mined40'] = df3['mined40'] * 2000 * df3['bitcoins/day']
    df3['mined50'] = 1 / (df3['HR50'][idInicial:idBMNfinal])
    df3['mined50'] = df3['mined50'] * 2000 * df3['bitcoins/day']
    df3['mined60'] = 1 / (df3['HR60'][idInicial:idBMNfinal])
    df3['mined60'] = df3['mined60'] * 2000 * df3['bitcoins/day']
    df3['mined70'] = 1 / (df3['HR70'][idInicial:idBMNfinal])
    df3['mined70'] = df3['mined70'] * 2000 * df3['bitcoins/day']
    df3['mined80'] = 1 / (df3['HR80'][idInicial:idBMNfinal])
    df3['mined80'] = df3['mined80'] * 2000 * df3['bitcoins/day']
    df3['mined90'] = 1 / (df3['HR90'][idInicial:idBMNfinal])
    df3['mined90'] = df3['mined90'] * 2000 * df3['bitcoins/day']
    df3['mined100'] = 1 / (df3['HR100'][idInicial:idBMNfinal])
    df3['mined100'] = df3['mined100'] * 2000 * df3['bitcoins/day']
    df3['accMined10'] = df3['accMined'].iloc[idActual] + df3['mined10'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined20'] = df3['accMined'].iloc[idActual] + df3['mined20'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined30'] = df3['accMined'].iloc[idActual] + df3['mined30'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined40'] = df3['accMined'].iloc[idActual] + df3['mined40'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined50'] = df3['accMined'].iloc[idActual] + df3['mined50'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined60'] = df3['accMined'].iloc[idActual] + df3['mined60'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined70'] = df3['accMined'].iloc[idActual] + df3['mined70'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined80'] = df3['accMined'].iloc[idActual] + df3['mined80'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined90'] = df3['accMined'].iloc[idActual] + df3['mined90'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['accMined100'] = df3['accMined'].iloc[idActual] + df3['mined100'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['buy1']= preciosTrancheBTC[0]
    df3['buy2']= preciosTrancheBTC[1]
    df3['buy3']= preciosTrancheBTC[2]
    df3['buy4']= preciosTrancheBTC[3]
    df3['buy5']= preciosTrancheBTC[4]
    df3['buy6']= preciosTrancheBTC[5]
    df3['buy7']= preciosTrancheBTC[6]
    df3['buy8']= preciosTrancheBTC[7]
    df3['buy1USD'] = 200000
    df3['buy2USD'] = 200000 # df3['bitcoin_price'][idTranche2:].multiply(preciosTrancheUSDenBTC[1])
    df3['buy3USD'] = 240000 # df3['bitcoin_price'][idTranche3:].multiply(preciosTrancheUSDenBTC[2])
    df3['buy4USD'] = 250000 # df3['bitcoin_price'][idTranche4:].multiply(preciosTrancheUSDenBTC[3])
    df3['buy5USD'] = 260000 # df3['bitcoin_price'][idTranche5:].multiply(preciosTrancheUSDenBTC[4])
    df3['buy6USD'] = 290000 # df3['bitcoin_price'][idTranche6:].multiply(preciosTrancheUSDenBTC[5])
    df3['buy7USD'] = 320000 # df3['bitcoin_price'][idTranche7:].multiply(preciosTrancheUSDenBTC[6])
    df3['buy8USD'] = 270000 # df3['bitcoin_price'][idTranche8:].multiply(preciosTrancheUSDenBTC[7])
    return df3

def addMoreRowsCustom(df3):
    df3['bitcoins/day'].loc[idHalving2024 + idActual:] = 475
    df3['mined'] = 1/(df3['NetworkHR'][idInicial:idBMNfinal])
    df3['mined'] =df3['mined'] * 2000 * df3['bitcoins/day']
    df3['accMined'] = df3['mined'][idInicial:idBMNfinal].cumsum(axis=0)
    df3['buy1']= preciosTrancheBTC[0]
    df3['buy2']= preciosTrancheBTC[1]
    df3['buy3']= preciosTrancheBTC[2]
    df3['buy4']= preciosTrancheBTC[3]
    df3['buy5']= preciosTrancheBTC[4]
    df3['buy6']= preciosTrancheBTC[5]
    df3['buy7']= preciosTrancheBTC[6]
    df3['buy8']= preciosTrancheBTC[7]
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
# df45 = addMoreRowsCustom(df35)
def chartIt(idBMNfinal):
    x1 = df4['date'][idInicial:idActual]
    x2 = df4['date'][idActual:idBMNfinal]
    x3 = df4['date'][idBMNInicial:idActual]
    y1 = df4['buy1'][idInicial:idActual]
    y12 = df4['buy1'][idActual:idBMNfinal]
    y13 = df4['buy4'][idInicial:idActual]
    y14 = df4['buy4'][idActual:idBMNfinal]
    y15 = df4['buy5'][idInicial:idActual]
    y16 = df4['buy5'][idActual:idBMNfinal]
    y17 = df4['buy6'][idInicial:idActual]
    y18 = df4['buy6'][idActual:idBMNfinal]
    y2 = df4['accMined'][idInicial:idActual]
    y22 = df4['accMined50'][idActual:idBMNfinal]
    y3 = df4['accMined80'][idActual:idBMNfinal]
    y4 = df4['accMined20'][idActual:idBMNfinal]
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
    y1 = df4['buy1USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 1
    y12 = df4['buy1USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 1 forecast
    y13 = df4['buy4USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 4
    y14 = df4['buy4USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 4 forecast
    y15 = df4['buy5USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 5
    y16 = df4['buy5USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 5 forecast
    y17 = df4['buy6USD'][idInicial:idActual] # valor del tranche si se comprasen BTC tranche 6
    y18 = df4['buy6USD'][idActual:idBMNfinal] # valor del tranche si se comprasen BTC tranche 6 forecast
    y2 = df4['accMined'][idInicial:idActual] * df4['bitcoin_price'][idInicial:idActual]
    y22 = df4['accMined50'][idActual:idBMNfinal] * df4['bitcoin_price'][idActual:idBMNfinal]
    y3 = df4['accMined80'][idActual:idBMNfinal] * df4['bitcoin_pricePos'][idActual:idBMNfinal]
    y4 = df4['accMined20'][idActual:idBMNfinal] * df4['bitcoin_priceNeg'][idActual:idBMNfinal]
    y5 = df4['BMN price'][idBMNInicial:idActual] * df4['bitcoin_price'][idBMNInicial:idActual]
    plt.figure(figsize=(11, 8))
    plt.plot(x1, y1, '-', label='USD price of Tranche 1')
    plt.plot(x2, y12, '--')
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

if __name__ == "__main__":
    chartIt(idBMNfinal)
    chartIt2(idBMNfinal)

print(df4[['date', 'accMined20', 'accMined50', 'accMined80', 'bitcoinP20', 'bitcoinP50', 'bitcoinP80' ]].iloc[idBMNfinal-1])
y22 = df4['accMined'][idActual:idBMNfinal] * df4['bitcoin_price'][idActual:idBMNfinal]
y3 = df4['accMined80'][idActual:idBMNfinal] * df4['bitcoin_pricePos'][idActual:idBMNfinal]
y4 = df4['accMined20'][idActual:idBMNfinal] * df4['bitcoin_priceNeg'][idActual:idBMNfinal]
y5 = df4['BMN price'][idBMNInicial:idActual] * df4['bitcoin_price'][idBMNInicial:idActual]

print(y22[idBMNfinal-1])
print(y3[idBMNfinal-1])
print(y4[idBMNfinal-1])
print(y5[idActual-1])
element = (((df4['accMined80'].iloc[idBMNfinal - 1]) * (df4['bitcoinP80'].iloc[idBMNfinal - 1])) - (df4['BMN price'][idActual] * df4['bitcoin_price'][idActual])) / (df4['BMN price'][idActual] * df4['bitcoin_price'][idActual])
print("element1 es: ", element)
element = (((element + 1) ** (1/(idBMNfinal - idActual))) ** (365)) - 1
print("element es: ", element)
df5 = pd.DataFrame(columns = ['HR\Price increases','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
df5['HR\Price increases'] = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']
x = 0
df5 = df5.set_index('HR\Price increases')
for row in range(len(df5)):
    for column in range(len(df5.columns)):
        element = (((df4['accMined' + str(tasasHR[row])].iloc[idBMNfinal - 1]) * (df4['bitcoinP' + str(tasasPrice[column])].iloc[idBMNfinal - 1])) - (
                    df4['BMN price'][idActual] * df4['bitcoin_price'][idActual])) / (df4['BMN price'][idActual] * df4['bitcoin_price'][idActual])
        element = (((element + 1) ** (1/(idBMNfinal - idActual))) ** (365)) - 1
        df5.iat[row, column] = str(round(100*element, 2))+"%"

print(tabulate(df5, headers = 'keys', tablefmt = 'psql'))
df5 = df5.style.background_gradient(cmap='PuBu', axis=None, vmin=30, vmax=70)
dfi.export(df5, 'mytable'+now+'.png', table_conversion='matplotlib')






