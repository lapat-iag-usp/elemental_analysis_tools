import csv 
import os

def getMasses(file_content,serial):

    lines = file_content.split("\n")

    # remove empty lines
    lines = [x for x in lines if x]

    r = {}
    for line in lines:
        cols = line.split(',')
            
        if str(cols[0]) == str(serial):
            r['total'] = float(cols[2])
            r[int(cols[3])] = float(cols[4])
            if len(cols) > 5:
                r[int(cols[5])] = float(cols[6])           
    return(r)

def getIds(file_content):
    lines = file_content.split("\n")

    # remove empty lines
    lines = [x for x in lines if x]

    r = []
    for line in lines:
        cols = line.split(',')
        r.append(cols[0])
    r.pop(0)
    return r

  
