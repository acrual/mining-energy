import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile("vicalvaro.xlsm")

pruebaFrame = xls.parse("NetworkHR", index_col=None, na_values=['NA'])
print(pruebaFrame.keys())
for i in range(len(pruebaFrame.keys())):
    if i >= 9:
        newFrame = pruebaFrame.pop('Unnamed: '+str(i))
plt.plot(range(1000, 6000), pruebaFrame['bitcoin_price'][1000:6000])
plt.show()
