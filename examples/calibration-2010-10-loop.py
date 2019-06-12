# ler informações micromatteri, que contém a densidade
import math
import pandas as pd
densidades = pd.read_csv('C:/Users/pc2/Documents/eas-master/eas-master/data/calibration/micromatter-table-iag.csv')
df = pd.DataFrame(densidades)
pto_txt = '.txt'
pto_csv = '.csv'
fatores=[]

#loop ler todos os elementos
for i in range(0,28): #trocar para len(df['serial']) depois

 
    d = df['density1'][i]

    # ler contagens do arquivos txt
    import sys
    import pathlib
    sys.path.append('lib')
    from winqxas import parseTxt
    #transformar nome do documento em str
    serial = str(df['serial'][i])
    doc_txt = 'C:/Users/pc2/Documents/eas-master/eas-master/data/calibration/2010-10/txt/'
    for j in range(len(serial)):
        doc_txt += serial[j]
    for j in range(len(pto_txt)):
        doc_txt += pto_txt[j]
    file_content = pathlib.Path(doc_txt).read_text()
    txt = parseTxt(file_content)
    N = txt['K']['peaks'][df['element1'][i]]
    #print(txt['K']['errors'][11])
    
    # ler corrente e tempo dos arquivos csv
    import shimadzu as sd
    doc_csv = 'C:/Users/pc2/Documents/eas-master/eas-master/data/calibration/2010-10/csv/'
    for j in range(len(serial)):
        doc_csv += serial[j]
    for j in range(len(pto_csv)):
        doc_csv += pto_csv[j]
    file_content = pathlib.Path(doc_csv).read_text()
    It = sd.parseCsv(file_content)
    I = It['current']
    tempo = It['livetime']

    # subtrair branco ??

    # caculcar fator de resposta ponto a ponto
    from responseFactor import responseFactor
    R = responseFactor(N,d,I,tempo)
    linha_fatores = [df['element1'][i], R]
    fatores.append(linha_fatores)
    
'''
    #calcular fator de resposta para element2 (se houver): verificar arquivos txt
    d = df['density2'][i]
    if not math.isnan(d):
        if df['element2'][i] < ?: 
            N = txt['K']['peaks'][df['element2'][i]]
        else:
            N = txt['L']['peaks'][df['element2'][i]]
        R = responseFactor(N,d,I,tempo)
        linha_fatores = [df['element2'][i], R]
        fatores.append(linha_fatores)
'''
print(fatores)
   
# Ajustar polinômio


