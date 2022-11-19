import openpyxl
import requests
import pandas as pd
import json
from datos import ultimaFecha
from datetime import datetime as dt

def dataframeExtract(que):
    url = 'https://api.blockchain.info/charts/'
    url = url + que
    res = requests.get(url, params={'timespan': '10weeks'})
    df = pd.read_json(res.text, convert_dates=['t'])
    return df

def extractHR():
    fes = []
    hrs = []
    df = dataframeExtract('hash-rate')
    res = df['values']
    for i in range(len(res)):
        res[i]['x'] = pd.to_datetime(res[i]['x'], unit='s')
        d = res[i]['x'].strftime("%d-%m-%Y")
        fes.append(d)
        hrs.append(df['values'][i]['y'])
    return fes, hrs

hr = extractHR()

def extractIngresos():
    fes = []
    rev = []
    df = dataframeExtract('miners-revenue')
    res = df['values']
    for i in range(len(res)):
        res[i]['x'] = pd.to_datetime(res[i]['x'], unit='s')
        d = res[i]['x'].strftime("%d-%m-%Y")
        fes.append(d)
        rev.append(df['values'][i]['y'])
    return fes, rev

ingresos = extractIngresos()

def extractPrecios():
    fes = []
    pre = []
    df = dataframeExtract('market-price')
    res = df['values']
    for i in range(len(res)):
        res[i]['x'] = pd.to_datetime(res[i]['x'], unit='s')
        d = res[i]['x'].strftime("%d-%m-%Y")
        fes.append(d)
        pre.append(df['values'][i]['y'])
    return fes, pre

precios = extractPrecios()

print(hr)
# def writeHR():
#     fechas, hashrates = extractHR()
#     wb = openpyxl.load_workbook('pruebas.xlsx')
#     sheet = wb['Sheet1']
#     for i in range(len(fechas)):
#         sheet.cell(row=i+2, column=5).value = fechas[i]
#         sheet.cell(row=i+2, column=6).value = hashrates[i]
#     wb.save('pruebas.xlsx')
#
# def writeRev():
#     fechas, revenues = extractIngresos()
#     wb = openpyxl.load_workbook('pruebas.xlsx')
#     sheet = wb['Sheet1']
#     for i in range(len(fechas)):
#         sheet.cell(row=i+2, column=8).value = fechas[i]
#         sheet.cell(row=i+2, column=9).value = revenues[i]
#     wb.save('pruebas.xlsx')
#
# def writePre():
#     fechas, precios = extractPrecios()
#     wb = openpyxl.load_workbook('pruebas.xlsx')
#     sheet = wb['Sheet1']
#     for i in range(len(fechas)):
#         sheet.cell(row=i+2, column=10).value = fechas[i]
#         sheet.cell(row=i+2, column=11).value = precios[i]
#     wb.save('pruebas.xlsx')
#
# writeHR()
# writeRev()
# writePre()
# for i in len(hr):
#     if hr[0] > ultimaFecha:
#         print(hr[0], hr[1])
#     if ingresos[0] > ultimaFecha:
#         print(ingresos[0], ingresos[1])
#     if precios[0] > ultimaFecha:
#         print(precios[0], precios[1])
