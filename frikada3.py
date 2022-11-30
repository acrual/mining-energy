from datos import *
import matplotlib.pyplot as plt


desde = input("Dime desde qué fecha quieres calcular. Formato YYYY-mm-dd. No pongas nada si es BMN: ")

if desde == "":
    print("Es BMN")
    print(tasaCentral, tasaNegativa, tasaPositiva)
else:
    print("NO ES BMN")
    print(tasaCentral, tasaNegativa, tasaPositiva)

idActual = df2['id'].iloc[-1]
idBMNfinal = idInicial + (3 * 365)
def addRows(ppio, fin, tasa, df2):
    bd = 950
    bd2 = bd/2
    tasa = ((1 + (tasa/100))**(1/365)) - 1
    for i in range(ppio, fin):
        if i > idHalving2024:
            bd = bd2
        rowPos = pd.DataFrame({'id': df2['id'].iloc[-1]+1, 'date': df2.iloc[-1]["date"]+ pd.Timedelta(1, unit='d'), 'NetworkHR': df2.iloc[-1]["NetworkHR"]*(1 + tasa), 'bitcoins/day': [bd],'bitcoin_price': df2.iloc[-1]["bitcoin_price"]*(1 + tasa), 'BMN price': df2.iloc[-1]["BMN price"], 'AsicPrice': df2.iloc[-1]["AsicPrice"], 'mined':950*2000/(df2['NetworkHR'].iloc[-1]),'buy1': preciosTrancheUSDenBTC[0], 'buy2': preciosTrancheUSDenBTC[1], 'buy3': preciosTrancheUSDenBTC[2], 'buy4': preciosTrancheUSDenBTC[3], 'buy5': preciosTrancheUSDenBTC[4], 'buy6': preciosTrancheUSDenBTC[5], 'buy7': preciosTrancheUSDenBTC[6], 'buy8': preciosTrancheUSDenBTC[7]})
        df2 = pd.concat([df2, rowPos], ignore_index=True)
    return df2

df2 = addRows(idActual, idBMNfinal, tasaPositiva, df2)
print(df2[-30:])
def chartIt(idBMNfinal):
        x1 = df2['date'][idInicial:idBMNfinal]
        actuals, forecast = x1 <= now, x1 >= now
        # visible, invisible = x1 <= now, x1 <= "13/01/2022"
        y1 = df2['buy1'][idInicial:idBMNfinal]
        y2 = df2['mined'][idInicial:idBMNfinal]
        x2 = df2['date'][idBMNInicial:idBMNfinal]
        plt.plot(x1[actuals], y1[actuals], '-', label='buy&hodl-Actuals')
        plt.plot(x1[forecast], y1[forecast], '--', label='buy&hodl-Forecast')
        plt.plot(x1[actuals], y2[actuals], '-', label='mine&hodl-Actuals')
        plt.plot(x1[forecast], y2[forecast], '--', label='mine&hodl-Forecast')
        # plt.plot(x1[visible], y3[visible], '-', label='BMNUSD Price')
        # plt.plot(x1[invisible], y3[invisible], '--', label='BMNUSD Price')
        plt.xlabel('days running')
        plt.ylabel('USD')
        plt.title('Mine vs Buy for BMN in USD')
        plt.legend()
        plt.show()
        plt.close('all')
chartIt(idBMNfinal)