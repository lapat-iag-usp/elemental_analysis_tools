"""
calculateResponseFactor: N/(density*current*livetime)
"""
import numpy as np

def responseFactor (N,density,current,livetime,sigma_N,sigma_density=0.05,sigma_current=0.05,sigma_livetime=0.05):
    
    R = N/(density*current*livetime)

    # Propagando incerteza
    sigR = R*np.sqrt((sigma_N/N)**2+(sigma_density)**2+(sigma_current)**2+(sigma_livetime)**2)
    
    return R,sigR #Retorna a incerteza do fator de resposta
