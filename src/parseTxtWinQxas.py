import re
import math

def parseTxtWinQxas(file_content):
    peak = {}
    error = {}

    lines = file_content.split("\n")
    
    Photopeaks_line = 4 # not sure if always...
    Photopeaks = int(lines[Photopeaks_line].split(',')[1].strip())

    for line in range(Photopeaks_line+1, Photopeaks_line + Photopeaks + 1):
        Z = int(lines[line].split(',')[0].strip())
        peak[Z] = int(lines[line].split(',')[2].strip())
        error[Z] = int(lines[line].split(',')[3].strip())
        
    # Incoherent scattering peaks
    if lines[Photopeaks_line + Photopeaks + 1].startswith('Incoherent'):
            for line in range(Photopeaks_line + Photopeaks + 2, len(lines)):
                if len(lines[line].strip()) != 0: 
                    Z = int(lines[line].split(',')[0].strip())
                    peak[Z] = peak[Z] + int(lines[line].split(',')[2].strip())
                    Incoherent_error = int(lines[line].split(',')[3].strip())
                    error[Z] = math.sqrt(Incoherent_error**2 + error[Z]**2)

    return({'peak': peak, 'error': error})
