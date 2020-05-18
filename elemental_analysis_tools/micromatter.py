"""
micromatter
===========

Micromatter: parse a csv file from a micromatter catalog with columns: serial,description,density,element1,mass1,element2,mass2

"""

import csv 
import os
import pathlib
import sys

def get(serial , file_content = None):
    """
    dddcd
    """

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
                if cols[6] != '':
                    r[int(cols[5])] = float(cols[6])
    return(r)

def getSerials(file_content = None):
    """
    ddasdasd
    """

    if file_content is None:
        file_content = defaultFile()

    lines = file_content.split("\n")

    # remove empty lines
    lines = [x for x in lines if x]

    r = []
    for line in lines:
        cols = line.split(',')
        r.append(cols[0])
    r.pop(0)
    return r

def serialsAsTuples(file_content = None):
    """
    dwd    ddd
    """
    if file_content is None:
        file_content = defaultFile()

    r = []
    for i in getSerials(file_content):
        r.append((i,i))
    return r

def defaultFile():
    """
    wedew
    """
    file_path = os.path.join(os.path.dirname(__file__), 'data/calibration/micromatter-table-iag.csv')
    return(pathlib.Path(file_path).read_text())

