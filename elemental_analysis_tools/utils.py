"""
utils
=====
utils functions
"""

import re

def parseCsv(file_content):
    """ 
    parseCsv
    ========

    parser a string file from Shimadzu analysis, returning a 
    dictonary with current, livetime and sample ID

    Parameters
    ----------
    file_content : str
        shimadzu output csv content 

    Returns
    -------
    dic
        dic with irradiation parameters

    """
    irradiation_parameters = {}
    irradiation_parameters['sample'] = file_content.split(',')[0].split(':')[1].replace("\"", "").strip()
    irradiation_parameters['current'] = re.sub(' +',' ',file_content.split(',')[12]).split(' ')[3]
    irradiation_parameters['current'] = int(re.findall('\d+', irradiation_parameters['current'])[0])
    irradiation_parameters['livetime'] = int(re.sub(' +',' ',file_content.split(',')[12]).split(' ')[13])
    return(irradiation_parameters)

