import re

def parseCsv(file_content):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    irradiation_parameters = {}
    irradiation_parameters['sample'] = file_content.split(',')[0].split(':')[1].replace("\"", "").strip()
    irradiation_parameters['current'] = re.sub(' +',' ',file_content.split(',')[12]).split(' ')[3]
    irradiation_parameters['current'] = int(re.findall('\d+', irradiation_parameters['current'])[0])
    irradiation_parameters['livetime'] = int(re.sub(' +',' ',file_content.split(',')[12]).split(' ')[13])
    return(irradiation_parameters)
