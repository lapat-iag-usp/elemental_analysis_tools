import math
import pandas as pd

densidades = pd.read_csv('data/calibration/micromatter-table-iag.csv')
df = pd.DataFrame(densidades)
pto_txt = '.txt'
pto_csv = '.csv'
fatores=[]

#loop ler todos os elementos
for i in range((len(df['serial']))):

    d = df['density1'][i]

    # ler contagens do arquivos txt
    import sys
    import pathlib
    sys.path.append('elemental_analysis_tools')
    from winqxas import parseTxt
    #transformar nome do documento em str
    serial = str(df['serial'][i])
    doc_txt = 'data/calibration/2010-10/txt/'
    for j in range(len(serial)):
        doc_txt += serial[j]
    for j in range(len(pto_txt)):
        doc_txt += pto_txt[j]
    file_content = pathlib.Path(doc_txt).read_text()
    txt = parseTxt(file_content)
    try:
        N = txt['K']['peaks'][df['element1'][i]]
        sigma_N = txt['K']['errors'][df['element1'][i]]
    except:
        pass
    #print(txt['K']['errors'][11])
    
    # ler corrente e tempo dos arquivos csv
    import shimadzu as sd
    doc_csv = 'data/calibration/2010-10/csv/'
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
    R,sigma_R = responseFactor(N,d,I,tempo,sigma_N)

    linha_fatores = [df['element1'][i], R,sigma_R]
    fatores.append(linha_fatores)
    

    #calcular fator de resposta para element2 
    d = df['density2'][i]
    try:
        N = txt['K']['peaks'][df['element1'][i]]
        sigma_N = txt['K']['errors'][df['element1'][i]]
    except:
        pass
    R,sigma_R = responseFactor(N,d,I,tempo,sigma_N)

    linha_fatores = [df['element1'][i], R,sigma_R]
    fatores.append(linha_fatores)

# Transformando fatores em dataframe, NaN removidos    
df = pd.DataFrame(fatores)
df = df.dropna()

fatores_finais = pd.DataFrame(columns=['Z','R','Error'])
# Médias e Incertezas
elementos = pd.unique(df[0])
for elemento in elementos:
    aux = df[df[0]==elemento]
    media = aux[1].mean(axis = 0) 

    total = 0
    for error in aux[2]:
        total += error**2
    erro = total**(1/2) 
    fatores_finais = fatores_finais.append({'Z':elemento, 'R':media, 'Error': erro} , ignore_index=True)

fatores_finais.to_csv('/home/thiago/output.csv', sep = ',',index = False)

#print(fatores_finais)

# Ajustar polinômio
from fitResponseFactor import fitResponseFactor
from fitResponseFactor import plotFit
from fitResponseFactor import experimentalData

experimental_data = pathlib.Path('/home/thiago/output.csv').read_text()
data = experimentalData(experimental_data)
Z = data['Z']
Y = data['Y']
Yerror = data['Yerror']

plt = plotFit(Z,Y,Yerror,start=11,end=50,degree=10,fit=True)

# Salvando
plt.savefig("/home/thiago/teste.png", dpi = 100)


