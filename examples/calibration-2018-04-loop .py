
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
    print(serial)
    doc_txt = 'data/calibration/2018-04/txt/'
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
    doc_csv = 'data/calibration/2018-04/csv/'
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

print(fatores)

repeticao = [fatores[0][0]]
i = 1
while i < len(fatores):
    if fatores[i][0] in repeticao:
        for j, word in enumerate(repeticao):
            if word == fatores[i][0]:
                indice = j
        media_R = (fatores[i][1]+fatores[indice][1])/2
        sigma_R = (fatores[i][2]**2 + fatores[indice][2]**2)**(1/2)
        fatores[indice][1] = media_R
        fatores[indice][2] = sigma_R
        del(fatores[i])
    else:
        repeticao.append(fatores[i][0])
        i += 1
print (fatores)  
   
# Ajustar polinômio


