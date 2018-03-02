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

def getSample(id):
    with open('app/scripts/tests/data/calibration/micromatter_IAGUSP.csv') as linhas:
        linhascsv = csv.reader(linhas,delimiter=',')
        for linha in linhascsv:
            if linha[0] == id:
                return(linha)
  
def bla():
    return sys.path[0]

