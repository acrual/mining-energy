import pandas as pd
from pruebas import now, extractHR, dataframeExtract
from bmnPriceSSwap import bmn

def extraerDatos():
    excel_file = pd.ExcelFile('DatosExcelMineria.xlsx')
    pd.set_option('display.float_format', lambda x: '%0.4f' % x)
    df2 = excel_file.parse('NetworkHR')
    df2 = df2.drop(df2.columns[[7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
    df2.fillna(value=0, inplace=True)
    return df2

df2 = extraerDatos()

# tranche 1 7–apr-21 eur 200k = 4.7952 BTC, precio por btc según esto de $41708.3750 pero en realidad de 58020.46
# tranche 2 17–jun21 eur 200k = 6.9758 BTC, precio por btc según esto de 28670.5467 pero en realidad de 38324.87
# tranche 3 17-sep-21 eur 240k = 5.9525 BTC, precio por btc según esto de 40319.1936 pero en realidad de 47785.26
# tranche 4 14–oct-21 eur 250k = 5.0356 BTC, precio por btc según esto de 49646.5168 pero en realidad de 57406.69
# tranche 5 18–oct-21 eur 260k = 4.8762 BTC, precio por btc según esto de 53320.2083 pero en realidad de 61546.21
# tranche 6 20-oct-21 eur 290k = 5.2808 BTC, precio por btc según esto de 54915.9218 pero en realidad de 64287.64
# tranche 7 12-nov-21 eur 320k = 5.7708 BTC, precio por btc según esto de 55451.5838 pero en realidad de 64838.81
# tranche 8 17-jan-22 eur 270k = 8.1394 BTC, precio por btc según esto de 33171.9782 pero en realidad de 43102.44


tasaCentral = 50
tasaPositiva = tasaCentral + 30
tasaNegativa = tasaCentral - 30
# datos iniciales para BMN
fechaInicial = "2021-07-07"
numMiners = 18.1818181818181818
kWMiners = 3.4
depreYears = 5
teraHashes = 110
fechaBMNInicial = "2022-01-12"
print(now, type(now))
print(df2.query("date == @fechaBMNInicial"))
idBMNInicial = int(float((df2.query("date == @fechaBMNInicial"))['id'].to_string(index=False)))
nhrInicial = float((df2.query('date == @fechaInicial'))['NetworkHR'].to_string(index=False))
idInicial = int(float((df2.query("date == @fechaInicial"))['id'].to_string(index=False)))
precioBMNPrimerDia = float((df2.query("date == @fechaInicial"))['BMN price'].to_string(index=False))
priceInicial = float((df2.query("date == @fechaInicial"))['bitcoin_price'].to_string(index=False))
bitcoinsDiaRed = float((df2.query("date == @fechaInicial"))['bitcoins/day'].to_string(index=False))
asicPrimerDia = float((df2.query("date == @fechaInicial"))['AsicPrice'].to_string(index=False))
costesTh = [100, 100, 120, 125, 130, 145, 160, 135]
preciosTrancheBTC = [4.7952, 6.9758, 5.9525, 5.0356, 4.8762, 5.2808, 5.7708, 8.1394]
preciosTrancheUSD = [200000, 200000, 240000, 250000, 260000, 290000, 320000, 270000]
preciosBTCFechas = [58020.46, 38324.87, 47785.26, 57406.69, 61546.21, 64287.64, 64838.81, 43102.44]
preciosTrancheUSDenBTC = []
# for i in range(len(preciosTrancheUSD)):
#     preciosTrancheUSDenBTC.append(preciosTrancheUSD[i]/preciosBTCFechas[i])
# print(preciosTrancheUSDenBTC)
# idActual = df2.query("date == @now")['id'].to_string(index=False)

# df2 = df2[4000:int(idActual)]
del df2['MinerHR']
del df2['bitcoins/miner']
ultimaFecha = df2.iloc[-15:]
print("La última fecha del excel es: ")
print(ultimaFecha)
print("La fecha de hoy es: " + now)
bd = []
hr = extractHR()
x = 0
print(len(hr), len(hr[0]), len(hr[1]), len(hr[2]), len(hr[3]), len(bmn[0][-len(hr[3]):]))
for i in range(len(hr[0])):
    hr[0][i] = pd.to_datetime(hr[0][i], format='%d-%m-%Y')  # .dt.time
    print(hr[0][i], type(hr[0][i]), df2['date'].iloc[-1], type(df2['date'].iloc[-1]))
    print(i)
    bd.append(hr[2][i] / hr[3][i])
    if hr[0][i] > df2['date'].iloc[-1]:
        print(hr[0][i])
        row = pd.DataFrame({'id': df2['id'].iloc[-1] + x, 'date': hr[0][i], 'NetworkHR': hr[1][i], 'bitcoins/day': bd[i],'bitcoin_price': hr[3][i], 'BMN price': bmn[0][-len(hr[3]):][i], 'AsicPrice': [21]})
        df2 = pd.concat([df2, [row]])
        x += 1
print(df2.iloc[-30:])
