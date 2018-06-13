import csv 
import os
import pathlib
import sys

def getMasses(serial , file_content = None):

    if file_content is None:
        file_content = defaultFile()

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

def getIds(file_content = None):

    if file_content is None:
        file_content = defaultFile()

    # remove empty lines
    lines = [x for x in lines if x]

    r = []
    for line in lines:
        cols = line.split(',')
        r.append(cols[0])
    r.pop(0)
    return r

def defaultFile():
    file_path='tests/data/calibration/micromatter.csv'
    return(pathlib.Path(file_path).read_text())

