[![Build Status](https://travis-ci.org/thiagogomesverissimo/eas.svg?branch=master)](https://travis-ci.org/thiagogomesverissimo/eas)

![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/thiagogomesverissimo/eas.svg) 
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/thiagogomesverissimo/eas.svg)

![GitHub issues](https://img.shields.io/github/issues/thiagogomesverissimo/eas.svg) 
![GitHub closed issues](https://img.shields.io/github/issues-closed/thiagogomesverissimo/eas.svg)

Documentation:

  - [https://eas.readthedocs.io/](https://eas.readthedocs.io/)

## Basic dev setup:

Libraries instalation:

    virtualenv -p python3 .virtualenv 
    . .virtualenv/bin/activate
    .virtualenv/bin/pip3 install -r requirements.txt

If necessary, recreate the requirements.txt:

    .virtualenv/bin/pip3 freeze > requirements.txt

Example of how to run tests, given you are at root directory:

     python3 tests/test_shimadzu.py



