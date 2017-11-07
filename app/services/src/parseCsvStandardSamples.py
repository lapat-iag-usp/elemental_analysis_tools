import re

def parseCsvStandardSamples(file_content):
    print(file_content)
    #irradiation_parameters = {}
    #irradiation_parameters['sample'] = file_content.split(',')[0].split(':')[1].replace("\"", "").strip()
    #irradiation_parameters['current'] = re.sub(' +',' ',file_content.split(',')[12]).split(' ')[3]
    #irradiation_parameters['current'] = int(re.findall('\d+', irradiation_parameters['current'])[0])
    #irradiation_parameters['livetime'] = int(re.sub(' +',' ',file_content.split(',')[12]).split(' ')[13])
    return(None)
