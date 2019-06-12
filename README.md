[![Build Status](https://travis-ci.org/thiagogomesverissimo/eas.svg?branch=master)](https://travis-ci.org/thiagogomesverissimo/eas)

![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/thiagogomesverissimo/eas.svg) 
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/thiagogomesverissimo/eas.svg)

![GitHub issues](https://img.shields.io/github/issues/thiagogomesverissimo/eas.svg) 
![GitHub closed issues](https://img.shields.io/github/issues-closed/thiagogomesverissimo/eas.svg)

Documentation:

  - [https://eas.readthedocs.io/](https://eas.readthedocs.io/)

## Basic dev setup:

Libraries instalation:

    virtualenv -p python3 .eas 
    . .eas/bin/activate
    pip3 install -r requirements.txt

If necessary, recreate the requirements.txt:

    pip3 freeze > requirements.txt

Example of how to run tests, given you are at root directory:

     python3 tests/test_shimadzu.py

Usecase examples collection are available at *examples* folder.

Tips:

Rename all files from shimadzu:

    rename 's/.2018*\d+//' *



