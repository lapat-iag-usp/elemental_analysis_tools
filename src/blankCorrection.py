import re
import math
import pathlib
import sys

def blankCorrection(irradiation_parameters, peaks, errors):
    """
    Receive a collection of blanks samples data (irradiation and fitting data) 
    and return the correction for each element Z. The key in irradiation_parameters, 
    peaks and errors must to be equal!
    """
    if not(irradiation_parameters.keys() == peaks.keys() == errors.keys()): 
        return False
        
    peaks_correction = {}
    errors_correction ={}
    peaks_by_it = {}
    errors_by_it ={}
    
    keys = irradiation_parameters.keys()
    for key in keys:
        it = irradiation_parameters[key]['livetime'] * irradiation_parameters[key]['current']
        peaks_by_it[key] = {k:v/it for k,v in peaks[key].items()}
        errors_by_it[key] = {k:v/it for k,v in errors[key].items()} 
        
    # seleciona todos Z disponíneis em todos arquivos
    all_Zs = [list(v.keys()) for v in peaks.values()]
    Zs = list(set([x for sublist in all_Zs for x in sublist]))
    Zs.sort()
    
    # Mean
    for Z in Zs:
        peaks_correction[Z] = sum(filter(None,[v.get(Z, None) for v in peaks_by_it.values()]))/len(keys)
        errors_correction[Z] = sum(filter(None,[v.get(Z, None) for v in errors_by_it.values()]))/len(keys)
        
    return({'peaks_correction': peaks_correction, 'errors_correction': errors_correction})
   

