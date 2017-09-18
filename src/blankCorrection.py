import re
import math
import pathlib
import sys

# importing 
sys.path.append('./')
from parseCsvShimadzu import parseCsvShimadzu
from parseTxtWinQxas import parseTxtWinQxas


def blankCorrection(csvs,txts):
    """
    Receive a list of strings that each one is ... 
    """
    peak = {}
    error = {}
    peak_return = {}
    error_return ={}
        
    keys = csvs.keys()
    for key in keys:
        csv_content = parseCsvShimadzu(csvs[key])
        it = csv_content['livetime'] * csv_content['current']
        
        txt_content = parseTxtWinQxas(txts[key])
        for i in txt_content:
            peak[key] = {k:v/it for k,v in txt_content['peak'].items()} 
            error[key] = {k:v/it for k,v in txt_content['error'].items()}

    # Trying to get a list of all Z (atomic number) taking in account 
    all_Zs = [list(v.keys()) for v in peak.values()]
    Zs = list(set([x for sublist in all_Zs for x in sublist]))
    Zs.sort()
    
    # Mean
    for Z in Zs:
        peak_return[Z] = sum(filter(None,[v.get(Z, None) for v in peak.values()]))/len(keys)
        error_return[Z] = sum(filter(None,[v.get(Z, None) for v in error.values()]))/len(keys)
        
    return({'peak': peak_return, 'error': error_return})

