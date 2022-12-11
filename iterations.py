from frikada3 import *

# tasasHR = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# tasasPrice = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# tasasDiariasHR = []
# tasasDiariasPrice = []
# for tasaHR in tasasHR:
#     tasasDiariasHR.append(((1 + (tasaHR / 100)) ** (1 / 365)) - 1)
# for tasaPrice in tasasPrice:
#     tasasDiariasPrice.append(((1 + (tasaPrice / 100)) ** (1 / 365)) - 1)

def addRows(bmn, ppio, fin, df4):
    if bmn == "bmnsi":
        for i in range(ppio, fin):
            if i == ppio:
                row1 = pd.DataFrame({'HR10': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[0]),'HR20': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[1]),
                                     'HR30': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[2]),'HR40': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[3]),
                                     'HR50': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[4]),'HR60': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[5]),
                                     'HR70': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[6]),'HR80': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[7]),
                                     'HR90': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[8]),'HR100': df4['NetworkHR'].iloc[-1]*(1 + tasasDiariasHR[9]),
                                     'bitcoinP10': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[0]),'bitcoinP20': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[1]),
                                     'bitcoinP30': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[2]),'bitcoinP40': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[3]),
                                     'bitcoinP50': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[4]),'bitcoinP60': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[5]),
                                     'bitcoinP70': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[6]),'bitcoinP80': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[7]),
                                     'bitcoinP90': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[8]),'bitcoinP100': df4['bitcoin_price'].iloc[-1]*(1 + tasasDiariasPrice[9])}, index=[0])
                df4 = pd.concat([df4, row1], ignore_index=True)
            else:
                row1 = pd.DataFrame({'HR10': df4['HR10'].iloc[-1] * (1 + tasasDiariasHR[0]),'HR20': df4['HR20'].iloc[-1] * (1 + tasasDiariasHR[1]),
                                     'HR30': df4['HR30'].iloc[-1] * (1 + tasasDiariasHR[2]),'HR40': df4['HR40'].iloc[-1] * (1 + tasasDiariasHR[3]),
                                     'HR50': df4['HR50'].iloc[-1] * (1 + tasasDiariasHR[4]),'HR60': df4['HR60'].iloc[-1] * (1 + tasasDiariasHR[5]),
                                     'HR70': df4['HR70'].iloc[-1] * (1 + tasasDiariasHR[6]),'HR80': df4['HR80'].iloc[-1] * (1 + tasasDiariasHR[7]),
                                     'HR90': df4['HR90'].iloc[-1] * (1 + tasasDiariasHR[8]),'HR100': df4['HR100'].iloc[-1] * (1 + tasasDiariasHR[9]),
                                     'bitcoinP10': df4['bitcoinP10'].iloc[-1] * (1 + tasasDiariasPrice[0]),'bitcoinP20': df4['bitcoinP20'].iloc[-1] * (1 + tasasDiariasPrice[1]),
                                     'bitcoinP30': df4['bitcoinP30'].iloc[-1] * (1 + tasasDiariasPrice[2]),'bitcoinP40': df4['bitcoinP40'].iloc[-1] * (1 + tasasDiariasPrice[3]),
                                     'bitcoinP50': df4['bitcoinP50'].iloc[-1] * (1 + tasasDiariasPrice[4]),'bitcoinP60': df4['bitcoinP60'].iloc[-1] * (1 + tasasDiariasPrice[5]),
                                     'bitcoinP70': df4['bitcoinP70'].iloc[-1] * (1 + tasasDiariasPrice[6]),'bitcoinP80': df4['bitcoinP80'].iloc[-1] * (1 + tasasDiariasPrice[7]),
                                     'bitcoinP90': df4['bitcoinP90'].iloc[-1] * (1 + tasasDiariasPrice[8]),'bitcoinP100': df4['bitcoinP100'].iloc[-1] * (1 + tasasDiariasPrice[9])}, index=[0])
                df4 = pd.concat([df4, row1], ignore_index=True)
    return df4

df4 = addRows('bmnsi', idActual, idBMNfinal, df4)

def addMoreRows(df4):
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


# print(df4[['HR20','HR50','HR80','NetworkHRNeg','NetworkHR','NetworkHRPos','bitcoinP20','bitcoin_priceNeg','bitcoin_price','bitcoinP80','bitcoin_pricePos']][-5:])
# print(df4[['HR80', 'NetworkHRPos']][idBMNfinal])
columnas = []
for col in df4.columns:
    # print(col, type(col))
    if col[0:2] == "HR":
        columnas.append(col)
print(columnas)
print(df4[columnas][idActual])