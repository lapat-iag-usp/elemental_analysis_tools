[![Build Status](https://travis-ci.org/thiagogomesverissimo/eas.svg?branch=master)](https://travis-ci.org/thiagogomesverissimo/eas)

![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/thiagogomesverissimo/eas.svg) 
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/thiagogomesverissimo/eas.svg)

![GitHub issues](https://img.shields.io/github/issues/thiagogomesverissimo/eas.svg) 
![GitHub closed issues](https://img.shields.io/github/issues-closed/thiagogomesverissimo/eas.svg)


Libraries instalation:

    virtualenv -p python3 vendor
    . vendor/bin/activate
    vendor/bin/pip3 install -r requirements.txt

If necessary, recreate the requirements.txt:

    vendor/bin/pip3 freeze > requirements.txt

Available classes:

 - WinQxas: parser a string file from WinQxas analysis, returning a dictonary dic['K']['peaks'] and 
 dic['K']['erros'] for K and L lines.

 - Shimadzu: parser a string file from Shimadzu analysis, returning a dictonary with current, livetime and sample ID.

 - BlankCorrection: Receive a collection of blanks samples data (irradiation and fitting data) 
    and return the correction for each element Z. The if for irradiation_parameters, 
    peaks and errors must to be equal.

 - Micromatter: parse a csv file from a micromatter catalog with columns: serial,description,density,element1,mass1,element2,mass2

 - calculateResponseFactor: N/(density*current*livetime)
 
 - calculateElementarDensity: N/(R*current*livetime)

 - adjustResponseFactor: Not implemented yet




