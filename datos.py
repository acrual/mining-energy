import pandas as pd
from pruebas import now, extractHR, dataframeExtract
from bmnPriceSSwap import bmn
import glob
import os
import os.path
def extraerDatos(que):
    excel_file = pd.ExcelFile(que)
    pd.set_option('display.float_format', lambda x: '%0.4f' % x)
    df2 = excel_file.parse('NetworkHR')
    # df2 = df2.drop(df2.columns[[7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
    df2.fillna(value=0, inplace=True)
    return df2

def ultimoFichero():
    latest_files = sorted(glob.iglob('DatosExcelMineria*.xlsx'), key=os.path.getmtime)
    return latest_files[-1]
ultF = ultimoFichero()
df2 = extraerDatos(ultF)

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
fechaHalving2024 = "25-03-2024"
idBMNInicial = int(float((df2.query("date == @fechaBMNInicial"))['id'].to_string(index=False)))
nhrInicial = float((df2.query('date == @fechaInicial'))['NetworkHR'].to_string(index=False))
idInicial = int(float((df2.query("date == @fechaInicial"))['id'].to_string(index=False)))
precioBMNPrimerDia = float((df2.query("date == @fechaInicial"))['BMN price'].to_string(index=False))
priceInicial = float((df2.query("date == @fechaInicial"))['bitcoin_price'].to_string(index=False))
bitcoinsDiaRed = float((df2.query("date == @fechaInicial"))['bitcoins/day'].to_string(index=False))
asicPrimerDia = float((df2.query("date == @fechaInicial"))['AsicPrice'].to_string(index=False))
idHalving2024 = int((pd.to_datetime(fechaHalving2024, format='%d-%m-%Y') - pd.to_datetime(now, format='%d-%m-%Y')) / pd.Timedelta(days=1))
print("idhalving es: ", idHalving2024, type(idHalving2024))
costesTh = [100, 100, 120, 125, 130, 145, 160, 135]
preciosTrancheBTC = [4.7952, 6.9758, 5.9525, 5.0356, 4.8762, 5.2808, 5.7708, 8.1394]
preciosTrancheUSD = [200000, 200000, 240000, 250000, 260000, 290000, 320000, 270000]
preciosBTCFechas = [58020.46, 38324.87, 47785.26, 57406.69, 61546.21, 64287.64, 64838.81, 43102.44]
preciosTrancheUSDenBTC = []
for i in range(len(preciosTrancheUSD)):
    preciosTrancheUSDenBTC.append(preciosTrancheUSD[i]/preciosBTCFechas[i])

ultimaFecha = df2.iloc[-15:]

bd = []
hr = extractHR()
for i in range(len(hr[0])):
    hr[0][i] = pd.to_datetime(hr[0][i], format='%d-%m-%Y')
    bd.append(hr[2][i] / hr[3][i])
    if hr[0][i] > df2['date'].iloc[-1]:
        row = pd.DataFrame({'id': df2['id'].iloc[-1]+1, 'date': hr[0][i], 'NetworkHR': hr[1][i], 'bitcoins/day': bd[i],'bitcoin_price': hr[3][i], 'BMN price': bmn[0][-len(hr[3]):][i], 'AsicPrice': [21]})
        df2 = pd.concat([df2, row], ignore_index=True)

print(df2.iloc[-30:])
df2.to_excel("DatosExcelMineria"+now+".xlsx", sheet_name="NetworkHR", index=False)
