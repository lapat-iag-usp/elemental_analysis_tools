import csv 
import os

def data():
    micromatter = []
    with open( os.path.join(os.path.dirname(__file__), 'data/micromatter.csv')) as linhas:
        linhascsv = csv.reader(linhas,delimiter=',')
        for linha in linhascsv:
            micromatter.append(linha)

    # remove cabeçalho
    micromatter.pop(0)
    return micromatter

def ids():
    retorno = []
    for i in data():
        retorno.append(i[0])
    return retorno

def idsTuplas():
    retorno = []
    for i in data():
        retorno.append((i[0],i[0]))
    return retorno

def get(id):
    for i in data():
        if str(i[0])==str(id):
            return i
  
