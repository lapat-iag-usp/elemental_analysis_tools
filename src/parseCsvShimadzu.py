import re

def parseCsvShimadzu(file_content):
    data = {}
    data['sample'] = file_content.split(',')[0].split(':')[1].replace("\"", "").strip()
    data['current'] = re.sub(' +',' ',file_content.split(',')[12]).split(' ')[3]
    data['current'] = int(re.findall('\d+', data['current'])[0])
    data['livetime'] = int(re.sub(' +',' ',file_content.split(',')[12]).split(' ')[13])
    return(data)
