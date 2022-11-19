from datos import .
import matplotlib.pyplot as plt


def datosTranche(numTranche):
    costeTh = costesTh[numTranche - 1]
    precioTrancheBTC = preciosTrancheBTC[numTranche - 1]
    precioTrancheUSD = preciosTrancheUSD[numTranche - 1]
    return costeTh, precioTrancheBTC, precioTrancheUSD

def btcAtStart(numTranche):
    totalCapex = 2000 * datosTranche(numTranche)[0]
    return totalCapex / priceInicial # cuantos bitcoin tendrías si hubieses destinado toda tu inversión en minería a buy&hodl

# este buy() asume que el número de bitcoins al principio sale de dividir el totalCapex entre el precio de btc inicial
# pero esto no tiene sentido: buy and hold de bitcoin tendrá que ser con el num inicial de btc y bh de USD con el núm inicial de btc pero calculado
# desde el precio inicial del tranche en USD

def buyandhodlColumn(df):
    x = []
    MinedUSDTranches = []
    btcprincipios = []
    for i in len(datos[0]):
        btcPrincipio = btcAtStart(i)
        btcprincipios.append(btcPrincipio)
        x = df['bitcoin_price'].multiply(btcPrincipio)
        MinedUSDTranches.append(x)
    return MinedUSDTranches, btcprincipios, x

def mineandhodlColumn(df):
    x = df['date'][idInicial:idFinal]
    NetworkHRplus = []
    NetworkHRcentral = []
    NetworkHRneg = []
    NetworkHRcentral.append((df['NetworkHR'][idActual + 1]) * (((tasaCentral / 100) + 1) ** (1 / 365)))
    for i in range(idFinal - (idActual + 1)):
        NetworkHRcentral.append(NetworkHRcentral[i] * (((tasaCentral / 100) + 1) ** (1 / 365)))
    NetworkHRneg.append((df['NetworkHR'][idActual + 1]) * (((tasaNegativa / 100) + 1) ** (1 / 365)))
    for i in range(idFinal - (idActual + 1)):
        NetworkHRneg.append(NetworkHRneg[i] * (((tasaNegativa / 100) + 1) ** (1 / 365)))
    NetworkHRplus.append((df['NetworkHR'][idActual + 1]) * (((tasaPositiva / 100) + 1) ** (1 / 365)))
    for i in range(idFinal - (idActual + 1)):
        NetworkHRplus.append(NetworkHRplus[i] * (((tasaPositiva / 100) + 1) ** (1 / 365)))
    # print(NetworkHRplus, NetworkHRneg, NetworkHRcentral)
    # df['Central'][0:idActual] = 0
    # df['Central'][idActual:idFinal] = pd.DataFrame(NetworkHRcentral, columns=['Central'])
    # df['Positive'][0:idActual] = 0
    # df['Positive'][idActual:idFinal] = pd.DataFrame(NetworkHRplus, columns=['Positive'])
    # df['Negative'][0:idActual] = 0
    # df['Negative'][idActual:idFinal] = pd.DataFrame(NetworkHRneg, columns=['Negative'])
    df.loc[:, 'bitcoins/day'] *= 2000
    df['MinedCentral'] = pd.DataFrame(NetworkHRcentral)
    # df['Mined'] = df['bitcoins/day'][idInicial:idFinal]/df['NetworkHR'][idInicial:idFinal]
    df['Cumulative Bitcoins'] = df['Mined'][idInicial:idFinal].cumsum()
    cols = ['Cumulative Bitcoins', 'bitcoin_price']
    df['MinedUSD'] = df.loc[:, cols].prod(axis=1)
    # print(df)
    return df['Cumulative Bitcoins'], df['Mined'], df['MinedUSD']

# print(idBMNInicial, nhrInicial, idInicial, precioBMNPrimerDia, priceInicial, bitcoinsDiaRed, asicPrimerDia)
def chartIt(opcion):
    if opcion == 1:
        x1 = df['date'][idInicial:idFinal]
        actuals, forecast = x1 <= now, x1 >= now
        visible, invisible = x1 <= now, x1 <= "13/01/2022"
        y1 = buy[0][0][idInicial:idFinal]
        y2 = mine[2][idInicial:idFinal]
        cols = ['BMN price', 'bitcoin_price']
        x2 = df['date'][idBMNInicial:idBMNFinal]
        df['BMNUSD'] = df.loc[:, cols].prod(axis=1)
        # print("probando esto: ", df['BMNUSD'][idBMNInicial - 5:idBMNInicial+50])
        # df['BMNUSD']= df['BMNUSD'].replace(0.0000,'')
        y3 = df['BMNUSD'][idInicial:idFinal]
        plt.plot(x1[actuals], y1[actuals], '-', label='buy&hodl-Actuals')
        plt.plot(x1[forecast], y1[forecast], '--', label='buy&hodl-Forecast')
        plt.plot(x1[actuals], y2[actuals], '-', label='mine&hodl-Actuals')
        plt.plot(x1[forecast], y2[forecast], '--', label='mine&hodl-Forecast')
        plt.plot(x1[visible], y3[visible], '-', label='BMNUSD Price')
        plt.plot(x1[invisible], y3[invisible], '--', label='BMNUSD Price')
        plt.xlabel('days running')
        plt.ylabel('USD')
        plt.title('Mine vs Buy for BMN in USD')
        plt.legend()
        plt.show()
        plt.close('all')

def menu():
    opcion = 100
    while True:
        print("1. Mine vs Hodl in USD for BMN for tranche 1")
        print("2. Mine vs Hodl in BTC for BMN")
        print("3. Network Hashrate (line) and accumulated BTC (bars)")
        print("4. Mine vs Hodl in USD for BMN for all tranches")
        print("5. 1 pero no BMN")
        print("6. 2 pero no BMN")
        print("7. 3 pero no BMN")
        print("8. 4 pero no BMN")
        print("9. Export Dataframe to CSV")
        print("0. Salir")
        opcion = input("¿Qué gráfica quieres?: ")
        if opcion != '0':
            buildChart(int(opcion))
        else:
            break

menu()