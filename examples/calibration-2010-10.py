# ler informações micromatteri, que contém a densidade
import pandas as pd
densidades = pd.read_csv('data/calibration/micromatter-table-iag.csv')
df = pd.DataFrame(densidades)
d = df['density1'][0]

# ler contagens do arquivos txt
import sys
import pathlib
sys.path.append('lib')
from winqxas import parseTxt
file_content = pathlib.Path('data/calibration/2010-10/txt/34662.txt').read_text()
txt = parseTxt(file_content)
N = txt['K']['peaks'][11]
#print(txt['K']['errors'][11])

# ler corrente e tempo dos arquivos csv
import shimadzu
file_content = pathlib.Path('data/calibration/2010-10/csv/34662.csv').read_text()
It = shimadzu.parseCsv(file_content)
I = It['current']
tempo = It['livetime']

# subtrair branco ??

# caculcar fator de resposta ponto a ponto
from responseFactor import responseFactor
R = responseFactor(N,d,I,tempo)
print(R)

# Ajustar polinômio
