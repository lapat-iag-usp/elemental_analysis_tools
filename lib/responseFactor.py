"""
calculateResponseFactor: N/(density*current*livetime)
"""
import numpy as np

def responseFactor(N,density,current,livetime):
    
    R = N/(density*current*livetime)
    return R

def responseFactorError(N,density,current,livetime):
    '''This function do the calc of Error'''
    
    #iniciando e atribuindo variáveis
    N = N
    Dens = density
    Current = current
    time = livetime
    #Calculando o fator de resposta
    R = responseFactor(N,Dens,Current,time)
    #Propagando incerteza
    sigR = R*np.sqrt((sigN/N)**2+(sigDens/Dens)**2+(sigCurrent/Current)**2+(sigTime/Time)**2) #propagação de incerteza
    
    return sigR #Retorna a incerteza do fator de resposta
