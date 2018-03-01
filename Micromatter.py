import csv 

def Micromatter(object):

    def csv2list():
        micromatter_IAGUSP = []
        with open('app/services/tests/data/calibration/micromatter_IAGUSP.csv') as linhas:
            linhascsv = csv.reader(linhas,delimiter=',')
            for linha in linhascsv:
                micromatter_IAGUSP.append(linha)

        # remove cabeçalho
        micromatter_IAGUSP.pop(0)
        return micromatter_IAGUSP


    def serials():
        micromatter_IAGUSP = []
        with open('app/scripts/tests/data/calibration/micromatter_IAGUSP.csv') as linhas:
            linhascsv = csv.reader(linhas,delimiter=',')
            for linha in linhascsv:
                micromatter_IAGUSP.append(linha[0])

        # remove cabeçalho
        micromatter_IAGUSP.pop(0)
        return micromatter_IAGUSP

    def serials4flask(self):
        retorno = []
        lista = serials()
        for i in lista:
            tupla = (i,i)
            retorno.append(tupla)
        return retorno

    def getSample(id):
        with open('app/scripts/tests/data/calibration/micromatter_IAGUSP.csv') as linhas:
            linhascsv = csv.reader(linhas,delimiter=',')
            for linha in linhascsv:
                if linha[0] == id:
                    return(linha)

