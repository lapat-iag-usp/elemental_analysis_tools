import numpy
import sys
from numpy.linalg import solve,inv
import io
import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def experimentalData(file_content):

    lines = file_content.split("\n")

    # remover header
    lines.pop(0)

    # remove empty lines
    lines = [x for x in lines if x]

    lines = numpy.array(lines)
    
    Z = numpy.array([])
    Y = numpy.array([])
    Yerror = numpy.array([])
    for line in lines:
        current_line = line.split(',')
        Z = numpy.append(Z,float(current_line[0]))
        Y = numpy.append(Y,float(current_line[1]))
        Yerror = numpy.append(Yerror,float(current_line[2]))

    return( {'Z': Z , 'Y': Y , 'Yerror': Yerror} )

def fitResponseFactor(Z,Y,Yerror, start=11,end=42, degree = 9):
    
    # Matrix X, each colunm like [1 z z^2 z^3 ... z^n] ...
    X = numpy.vstack([Z**j for j in range(degree)]).T

    # Variance of Y
    VY = numpy.zeros((len(Y),len(Y)),float)
    numpy.fill_diagonal(VY,Yerror**2)

    # Variance of A 
    VA = inv(numpy.dot(numpy.dot(X.T,inv(VY)),X)) 

    # Coefficients
    A = numpy.dot(numpy.dot(numpy.dot(VA,X.T),inv(VY)),Y)

    # square root of VA diagonal gives the A errors
    coefficients_errors = numpy.sqrt(numpy.diagonal(VA))

    # atomic numbers
    Zadjusted = numpy.array(range(start,end)) 

    # Response Factor adjusted
    Xadjusted = numpy.vstack([Zadjusted**j for j in range(degree)]).T
    Yadjusted = numpy.dot(Xadjusted,A)

    # covariance matrix of Yadjusted (CYadjusted)
    CYadjusted = numpy.dot(numpy.dot(Xadjusted,VA),Xadjusted.T)

    # error
    YadjustedError =  numpy.sqrt(numpy.diagonal(CYadjusted))

    # dataframe to export
    response_factor_numpy = numpy.vstack((Zadjusted.astype(int),Yadjusted,YadjustedError)).T
    export = pd.DataFrame({
        'Z': response_factor_numpy[:, 0], 
        'Y': response_factor_numpy[:, 1],
        'Yerror': response_factor_numpy[:, 2]
    })
    export["Z"] = export["Z"].astype(int)
    
    return({
        'coefficients': A, 
        'coefficients_errors': coefficients_errors,
        'export': export
    })

def plotFit(Z,Y,Yerror,start=11,end=42,degree=9,fit=False, line='K'):

    plt.figure(1)

    #Limpar workspace
    plt.clf()

    #Elemento no eixo X
    plt.xlim(start-2,end+5)

    #Colocando Título
    plt.title('Linha ' + str(line))

    # Labels
    plt.ylabel('Fator de Resposta')
    plt.xlabel('Z')

    #Limites do eixo Y (eixo do fator de resposta)
    #plt.ylim(min(Y)-0.05,max(Y)+0.05)

    #Plot dos pontos experimentais
    plt.plot(Z,Y,'bD')

    #colocar barras de erros nos pontos experimentais
    plt.errorbar(Z,Y,yerr=Yerror,ecolor='b',fmt='none')

    # Ajustando Curva
    if fit:
        coefficients = fitResponseFactor(Z,Y,Yerror,start,end,degree)['coefficients']

        # Calculo do fator de resposta em um espaço com mais pontos, para plotar gráfico
        Zplot = numpy.linspace(start,end,600) 
        Xplot = numpy.vstack([Zplot**j for j in range(degree)]).T
        Yplot = numpy.dot(Xplot,coefficients)
    
        # Plot da curva ajustada
        plt.plot(Zplot,Yplot,'r-')

    # Configurando tamanho ?
    figure = plt.gcf()
    figure.set_size_inches(8, 6)
    
    return plt



