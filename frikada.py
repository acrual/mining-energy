import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=2)
now = str(d.strftime('%Y-%m-%d'))

def bmnStatus():
    bmnsn = input("¿Es BMN1? s/n: ")
    hostingsn = input("Es hosting? s/n: ")
    if hostingsn == 'n':
        pool = input("introduce el porcentaje que se lleva el pool: ")
    return bmnsn, hostingsn, pool

def popularNoBMN():
    fechaInicial = input("Desde que fecha? dd-mm-yyyy: ")
    numMiners = float(input("Cuántos miners?: "))
    terasMiner = float(input("Cuántos teras por miner: "))
    kWMiners = float(input("Cuanto consume cada miner=: "))
    depreYears = float(input("Cuántos años de vida útil los miners?: "))
    costeTh = float(input("Cuánto has pagado por Th?: "))
    completarCostes = input("Quieres añadir setup costs?(s/n): ")
    if completarCostes == 's':
        setUpCosts = input("Cuánto setup costs?: ")
    else:
        setUpCosts = 0
    return fechaInicial, numMiners, terasMiner, kWMiners, depreYears, costeTh, setUpCosts

def tranche(numTranche):
    if numTranche == '1':
        costeTh = 100
    elif numTranche == '2':
        costeTh = 100
    elif numTranche == '3':
        costeTh = 120
    elif numTranche == '4':
        costeTh = 125
    elif numTranche == '5':
        costeTh = 130
    elif numTranche == '6':
        costeTh == 145
    elif numTranche == '7':
        costeTh = 160
    elif numTranche == '8':
        costeTh = 135
    print(costeTh)
    print("Has pagado ", costeTh * 2000, "dólares")
    return costeTh

def popularSiBMN():
    fechaInicial = "2021-07-07"
    numMiners = 18.1818181818181818
    kWMiners = 3.4
    depreYears = 5
    teraHashes = 110
    numTranche = input("qué número de tranche?: ")
    costeTh = tranche(numTranche)
    return fechaInicial, numMiners, kWMiners, depreYears, costeTh, teraHashes

def calcularPrimerDia(bmnsn, datos):
    excel_file = pd.ExcelFile('BSMiningExperiments.xlsm')
    pd.set_option('display.float_format', lambda x: '%0.4f' % x)
    df = excel_file.parse('NetworkHR')
    df = df.drop(df.columns[[7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
    df.fillna(value=0, inplace=True)
    # df = df.convert_objects(convert_numeric=True)
    if bmnsn[0] == 's':
        fechaInicial = datos[0]
        fechaBMNInicial = "2022-01-12"
        idBMNInicial = int((df.query("date == @fechaBMNInicial"))['id'].to_string(index=False))
        nhrInicial = float((df.query('date == @fechaInicial'))['NetworkHR'].to_string(index=False))
        idInicial = int((df.query("date == @fechaInicial"))['id'].to_string(index=False))
        precioBMNPrimerDia = float((df.query("date == @fechaInicial"))['BMN price'].to_string(index=False))
        priceInicial = float((df.query("date == @fechaInicial"))['bitcoin_price'].to_string(index=False))
        bitcoinsDiaRed = float((df.query("date == @fechaInicial"))['bitcoins/day'].to_string(index=False))
        asicPrimerDia = float((df.query("date == @fechaInicial"))['AsicPrice'].to_string(index=False))
        hrIncreases = [20, 20, 20, 20, 20]
        priceIncreases = [30, 30, 30, 30, 30]
    else:
        fechaInicial = datos[0]
        hrIncreases = [20, 20, 20, 20, 20]
        priceIncreases = [30, 30, 30, 30, 30]
        nhrInicial = float((df.query('date == @fechaInicial'))['NetworkHR'].to_string(index=False))
        nhrInicial = nhrInicial
        idInicial = int((df.query("date == @fechaInicial"))['id'].to_string(index=False))
        precioBMNPrimerDia = 0
        priceInicial = float((df.query("date == @fechaInicial"))['bitcoin_price'].to_string(index=False))
        bitcoinsDiaRed = float((df.query("date == @fechaInicial"))['bitcoins/day'].to_string(index=False))
        idBMNInicial = 0
        asicPrimerDia = float((df.query("date == @fechaInicial"))['AsicPrice'].to_string(index=False))
    return idInicial, nhrInicial, priceInicial, bitcoinsDiaRed, precioBMNPrimerDia, asicPrimerDia, df, hrIncreases, priceIncreases, idBMNInicial


def btcAtStart(bmnsn, cosas, calculosPrimerDia):
    if bmnsn[0] == 's':
        totalCapex = 2000 * cosas
    elif bmnsn[0] == 'n':
        hardwareCost = calculosPrimerDia[5] * datos # asicprice * numterasminer * numminers
        totalCapex = hardwareCost + calculosPrimerDia[5]

    return totalCapex / calculosPrimerDia[2]

tenemosDatos = False

while tenemosDatos==False:
    bmnsn = bmnStatus()
    if bmnsn[0] == 's':
        datos = popularSiBMN()
        calculosPrimerDia = calcularPrimerDia('s', datos)
        totalCapex = 2000 * calculosPrimerDia[4]
        btcPrincipio = totalCapex / calculosPrimerDia[2]
        duracion = 365*3
        numMiners = datos[1]
        tenemosDatos = True
    elif bmnsn[0] == 'n':
        datos = popularNoBMN()
        calculosPrimerDia = calcularPrimerDia('n', datos)
        hardwareCost = calculosPrimerDia[0] * calculosPrimerDia[1] * calculosPrimerDia[4]
        totalCapex = hardwareCost + calculosPrimerDia[5]
        btcPrincipio = totalCapex / calculosPrimerDia[2]
        duracion = 365*5
        numMiners = datos[1]
        terasTotales = numMiners * datos[5]
        tenemosDatos = True
    else:
        print("estás empanado, repetimos: ")

df = calculosPrimerDia[6]
idActual = int((df.query("date == @now"))['id'].to_string(index=False))
fechaInicial = datos[0]
nhrInicial = datos[1]
priceInicial = datos[2]
precioBMNInicial = datos[3]
asicsInicial = datos[4]
df = calculosPrimerDia[6]
idInicial = calculosPrimerDia[0]
idFinal = idInicial + duracion
idBMNInicial = calculosPrimerDia[9]
idBMNFinal = idActual
btcPrincipio = btcAtStart('s', datos[4], calculosPrimerDia)
bitcoinsMinadosHoy = df['bitcoins/day'][idInicial:idFinal]
incHRDiario1 = (float(calculosPrimerDia[7][0])/100 + 1)**(1/365)
incHRDiario2 = (float(calculosPrimerDia[7][1])/100 + 1)**(1/365)
incHRDiario3 = (float(calculosPrimerDia[7][2])/100 + 1)**(1/365)
incHRDiario4 = (float(calculosPrimerDia[7][3])/100 + 1)**(1/365)
incHRDiario5 = (float(calculosPrimerDia[7][4])/100 + 1)**(1/365)
incPRDiario1 = (float(calculosPrimerDia[8][0])/100 + 1)**(1/365)
incPRDiario2 = (float(calculosPrimerDia[8][1])/100 + 1)**(1/365)
incPRDiario3 = (float(calculosPrimerDia[8][2])/100 + 1)**(1/365)
incPRDiario4 = (float(calculosPrimerDia[8][3])/100 + 1)**(1/365)
incPRDiario5 = (float(calculosPrimerDia[8][4])/100 + 1)**(1/365)

def buyandhodlColumn(df, bmnsn):
    if bmnsn[0] == 's':
        costesTh = [100, 100, 120, 125, 130, 145, 160, 135]
        x = []
        MinedUSDTranches = []
        btcprincipios = []
        for i in costesTh:
            btcPrincipio = btcAtStart('s', i, calculosPrimerDia)
            print(btcPrincipio, (btcPrincipio))
            btcprincipios.append(btcPrincipio)
            x = df['bitcoin_price'].multiply(btcPrincipio)
            MinedUSDTranches.append(x)
            # else:
            #     btcPrincipio = btcAtStart('n', 0, calculosPrimerDia)
            #     x = df['bitcoin_price'].multiply(btcPrincipio)
    else:
        btcPrincipio = btcAtStart('n', 0, calculosPrimerDia)
        print(type(df['bitcoin_price']), type(btcPrincipio))
        x = df['bitcoin_price'].multiply(btcPrincipio)
        print("vale")
        MinedUSDTranches = 0
    return MinedUSDTranches, btcprincipios, x

def mineandhodlColumn(df, bmnsn):
    x = df['date'][idInicial:idFinal]
    if bmnsn[0] == 's':
        df.loc[:, 'bitcoins/day'] *= 2000
        df['Mined'] = df['bitcoins/day'][idInicial:idFinal]/df['NetworkHR'][idInicial:idFinal]
        df['Cumulative Bitcoins'] = df['Mined'][idInicial:idFinal].cumsum()
        cols = ['Cumulative Bitcoins', 'bitcoin_price']
        df['MinedUSD'] = df.loc[:, cols].prod(axis=1)
    # else:
    #     df.loc[:, 'bitcoins/day'] *= (df['bitcoin_price'][idInicial:idFinal] * (terasTotales * bitcoinsMinadosHoy))
    #     df['Mined'] = df['bitcoins/day'][idInicial:idFinal] / df['NetworkHR'][idInicial:idFinal]
    #     df['Cumulative Bitcoins'] = df['Mined'][idInicial:idFinal].cumsum()
    #     cols = ['Cumulative Bitcoins', 'bitcoin_price']
    #     df['MinedUSD'] = df.loc[:, cols].prod(axis=1)
    return df['Cumulative Bitcoins'], df['Mined'], df['MinedUSD']

def buildChart(opcion):
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
        plt.plot(x1[actuals], y1[actuals], '-', label = 'buy&hodl-Actuals' )
        plt.plot(x1[forecast], y1[forecast], '--', label = 'buy&hodl-Forecast' )
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
    elif opcion == 2:
        print(idBMNInicial, idBMNFinal)
        x1 = df['date'][idInicial:idFinal]
        x2 = df['date'][idBMNInicial:idBMNFinal]
        actuals, forecast = x1 <= now, x1 >= now
        df['btcStart'] = 4.7952 # buy[1][0]
        y1 = mine[0][idInicial:idFinal]
        y2 = df['btcStart'][idInicial:idFinal]
        y3 = df['BMN price'][idBMNInicial:idBMNFinal]
        df['btcStart'] = 6.9758 # buy[1][1]
        y4 = df['btcStart'][idInicial:idFinal] # tranche 2
        df['btcStart'] = 5.9525 # buy[1][2]
        y5 = df['btcStart'][idInicial:idFinal]  # tranche 3
        df['btcStart'] = 5.0356 # buy[1][3]
        y6 = df['btcStart'][idInicial:idFinal]  # tranche 4
        df['btcStart'] = 4.8762 # buy[1][4]
        y7 = df['btcStart'][idInicial:idFinal]  # tranche 5
        df['btcStart'] = 5.2808 # buy[1][5]
        y8 = df['btcStart'][idInicial:idFinal]  # tranche 6
        df['btcStart'] = 5.7708 # buy[1][6]
        y9 = df['btcStart'][idInicial:idFinal]  # tranche 7
        df['btcStart'] = 8.1394 # buy[1][7]
        y10 = df['btcStart'][idInicial:idFinal]  # tranche 8
        plt.plot(x1[actuals], y1[actuals], '-', label='AccumulatedBTC-Actuals')
        plt.plot(x1[forecast], y1[forecast], '--', label='Accumulated-Forecast')
        # plt.plot(x1[actuals], y2[actuals], '-', label='hodledBTC tranche 1')
        plt.plot(x1, y2, '-', label='BTCBMN price tranche 1')
        plt.plot(x2, y3, '-', label='BMNBTC Price in SideSwap')
        plt.plot(x1, y4, '-', label='BTCBMN price tranche 2')
        plt.plot(x1, y5, '-', label='BTCBMN price tranche 3')
        plt.plot(x1, y6, '-', label='BTCBMN price tranche 4')
        plt.plot(x1, y7, '-', label='BTCBMN price tranche 5')
        plt.plot(x1, y8, '-', label='BTCBMN price tranche 6')
        plt.plot(x1, y9, '-', label='BTCBMN price tranche 7')
        plt.plot(x1, y10, '-', label='BTCBMN price tranche 8')
        plt.xlabel('days running')
        plt.ylabel('BTC')
        plt.title('Mine vs Buy for BMN in BTC')
        plt.legend()
        plt.show()
        plt.close('all')
    elif opcion == 3:
        # define colors to use
        col1 = 'steelblue'
        col2 = 'red'
        # define subplots
        fig, ax = plt.subplots()
        # add first line to plot
        x1 = df['date'][idInicial:idFinal]
        actuals, forecast = x1 <= now, x1 >= now
        y1 = df['NetworkHR'][idInicial:idFinal]
        ax.plot(x1, y1, color=col1)
        plt.plot(x1[actuals], y1[actuals], '-', label='Hashrate')
        plt.plot(x1[forecast], y1[forecast], '--', label='Forecasted hashrate')
        plt.legend()
        # add x-axis label
        ax.set_xlabel('Days running', fontsize=12)
        # add y-axis label
        ax.set_ylabel('NetworkHR', color=col1, fontsize=12)
        # define second y-axis that shares x-axis with current plot
        ax2 = ax.twinx()
        # add second line to plot
        y2 = mine[1][idInicial:idFinal]
        ax2.plot(x1, y2, color=col2)
        ax2.set_ylabel('Number of BTC', color=col2, fontsize=12)
        plt.ylim(0, 0.1)
        plt.bar(x1, y2, label='generated BTC')
        plt.title('Network Hashrate y número de BTC minados')
        plt.legend()
        plt.show()
        plt.close('all')
    elif opcion == 4:
        x1 = df['date'][idInicial:idFinal]
        actuals, forecast = x1 <= now, x1 >= now
        visible, invisible = x1 <= now, x1 >= fechaInicial
        y1 = buy[0][0][idInicial:idFinal]
        y2 = mine[2][idInicial:idFinal]
        cols = ['BMN price', 'bitcoin_price']
        df['BMNUSD'] = df.loc[:, cols].prod(axis=1)
        # y3 = df['BMNUSD'][idInicial: idFinal]
        y4 = y1 # tranche 2 es igual a tranche 1
        y5 = buy[0][2][idInicial:idFinal] # tranche 3
        y6 = buy[0][3][idInicial:idFinal] # tranche 4
        y7 = buy[0][4][idInicial:idFinal]  # tranche 5
        y8 = buy[0][5][idInicial:idFinal]  # tranche 6
        y9 = buy[0][6][idInicial:idFinal]  # tranche 7
        y10 = buy[0][7][idInicial:idFinal]  # tranche 8
        plt.plot(x1[actuals], y1[actuals], '-', label='BMNBTC price tranche1')
        plt.plot(x1[forecast], y1[forecast], '--')
        plt.plot(x1[actuals], y2[actuals], '-', label='mine&hodl-Actuals')
        plt.plot(x1[forecast], y2[forecast], '--', label='mine&hodl-Forecast')
        # plt.plot(x1[visible], y3[visible], '-', label='BMNUSD Price')
        # plt.plot(x1[invisible], y3[invisible], ' ', label='')
        plt.plot(x1[actuals], y4[actuals], '-', label='BMNBTC price tranche2')
        plt.plot(x1[forecast], y4[forecast], '--')
        plt.plot(x1[actuals], y5[actuals], '-', label='BMNBTC price tranche3')
        plt.plot(x1[forecast], y5[forecast], '--')
        plt.plot(x1[actuals], y6[actuals], '-', label='BMNBTC price tranche4')
        plt.plot(x1[forecast], y6[forecast], '--')
        plt.plot(x1[actuals], y7[actuals], '-', label='BMNBTC price tranche5')
        plt.plot(x1[forecast], y7[forecast], '--')
        plt.plot(x1[actuals], y8[actuals], '-', label='BMNBTC price tranche6')
        plt.plot(x1[forecast], y8[forecast], '--')
        plt.plot(x1[actuals], y9[actuals], '-', label='BMNBTC price tranche7')
        plt.plot(x1[forecast], y9[forecast], '--')
        plt.plot(x1[actuals], y10[actuals], '-', label='BMNBTC price tranche8')
        plt.plot(x1[forecast], y10[forecast], '--')
        plt.xlabel('days running')
        plt.ylabel('USD')
        plt.title('Mine vs Buy for BMN in USD')
        plt.legend()
        plt.show()
        plt.close('all')
    # elif opcion == 5:
    #     x1 = df['date'][idInicial:idFinal]
    #     actuals, forecast = x1 <= now, x1 >= now
    #     visible, invisible = x1 <= now, x1 <= "13/01/2022"
    #     y1 = buy[2][idInicial:idFinal]
    #     y2 = mine[2][idInicial:idFinal]
    #     plt.plot(x1[actuals], y1[actuals], '-', label='buy&hodl-Actuals')
    #     plt.plot(x1[forecast], y1[forecast], '--', label='buy&hodl-Forecast')
    #     plt.plot(x1[actuals], y2[actuals], '-', label='mine&hodl-Actuals')
    #     plt.plot(x1[forecast], y2[forecast], '--', label='mine&hodl-Forecast')
    #     plt.xlabel('days running')
    #     plt.ylabel('USD')
    #     plt.title('Mine vs Buy in USD')
    #     plt.legend()
    #     plt.show()
    #     plt.close('all')
    elif opcion == 9:
        df.to_csv('export.csv')


buy = buyandhodlColumn(df, bmnsn)
mine = mineandhodlColumn(df, bmnsn)

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





