import re

def parseTxtWinQxas(file_content):
    peak = {}
    error = {}

    lines = file_content.split("\n")
    Photopeaks = int(lines[4].split(',')[1].strip())

    for line in range(5, 5 + Photopeaks):
        Z = int(lines[line].split(',')[0].strip())
        peak[Z] = int(lines[line].split(',')[2].strip())
        error[Z] = int(lines[line].split(',')[3].strip())
        
    # Incoherent scattering peaks
    if lines[5 + Photopeaks + 1].startswith('Incoherent'):
        Incoherents = int(lines[5 + Photopeaks + 1].split(',')[1].strip())
        print('##############')
        print(Incoherents)
    #data['sample'] = file_content.split(',')[0].split(':')[1].replace("\"", "").strip()
    #data['current'] = re.sub(' +',' ',file_content.split(',')[12]).split(' ')[3]
    #data['current'] = int(re.findall('\d+', data['current'])[0])
    #data['livetime'] = int(re.sub(' +',' ',file_content.split(',')[12]).split(' ')[13])
    return({'peak': peak, 'error': error})
