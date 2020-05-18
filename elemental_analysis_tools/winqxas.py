"""
winqxas
=======
WinQxas: parser a string file from WinQxas analysis, returning a dictonary dic['K']['peaks'] and dic['K']['erros'] for K and L lines.
"""
import re
import math
import pyxray

def checkLine(Z,energy):
    """
    TODO: doc
    """
    Ka1=False
    try:
        Ka1 = pyxray.xray_transition_energy_eV(Z, 'Ka1')/1000
    except:
        pass
    if Ka1:
        if energy > (Ka1-2.0) and energy < (Ka1+2.0):
            return('K')
        else:
            return('L')
    else:
        return('L')

def parseTxt(file_content):
    r = {
            'K': {'peaks': {}, 'errors': {}},
            'L': {'peaks': {}, 'errors': {}}
        }

    lines = file_content.split("\n")
    
    Photopeakss_line = 4 # not sure if always...
    Photopeakss = int(lines[Photopeakss_line].split(',')[1].strip())

    for line in range(Photopeakss_line+1, Photopeakss_line + Photopeakss + 1):
        Z = int(lines[line].split(',')[0].strip())
        energy = float(lines[line].split(',')[1].strip())
        peak = int(lines[line].split(',')[2].strip())
        error = int(lines[line].split(',')[3].strip())
        line=checkLine(Z,energy)

        r[line]['peaks'][Z] = peak
        r[line]['errors'][Z] = error
    """  
    # Incoherent scattering peaks
    if lines[Photopeakss_line + Photopeakss + 1].startswith('Incoherent'):
            for line in range(Photopeakss_line + Photopeakss + 2, len(lines)):
                if len(lines[line].strip()) != 0: 
                    iZ = int(lines[line].split(',')[0].strip())
                    ienergy = float(lines[line].split(',')[1].strip())
                    ipeak = int(lines[line].split(',')[2].strip())
                    ierror = int(lines[line].split(',')[3].strip())
                    iline=checkLine(iZ,ienergy)
                
                    if r[iline]['peaks'][iZ]:
                        r[iline]['peaks'][iZ] = r[iline]['peaks'][iZ] + ipeak
    
                    if r[iline]['errors'][iZ]:
                        r[iline]['errors'][iZ] = math.sqrt(ierror**2 + r[iline]['errors'][iZ]**2)
    """
    return(r)
