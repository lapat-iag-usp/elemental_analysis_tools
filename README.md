[![Build Status](https://travis-ci.org/thiagogomesverissimo/elemental-analysis-scripts.svg?branch=master)](https://travis-ci.org/thiagogomesverissimo/elemental-analysis-scripts)

![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/thiagogomesverissimo/elemental-analysis-scripts.svg) 
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/thiagogomesverissimo/elemental-analysis-scripts.svg)

![GitHub issues](https://img.shields.io/github/issues/thiagogomesverissimo/elemental-analysis-scripts.svg) 
![GitHub closed issues](https://img.shields.io/github/issues-closed/thiagogomesverissimo/elemental-analysis-scripts.svg)

Documentation:

  - [https://elemental-analysis-scripts.readthedocs.io/](https://elemental-analysis-scripts.readthedocs.io/)

## Basic dev setup:

Libraries instalation:

    virtualenv -p python3 .elemental-analysis-scripts 
    . .elemental-analysis-scripts/bin/activate
    pip3 install -r requirements.txt

If necessary, recreate the requirements.txt:

    pip3 freeze > requirements.txt

Example of how to run tests, given you are at root directory:

     python3 tests/test_shimadzu.py

Usecase examples collection are available at *examples* folder.

Tips:

Rename a file from ki_34668_16p.20180402143731.csv to 34668.csv:

    rename 's/.2018*\d+//' *
    rename 's/^(.*?)\_//' *
    rename 's/_16p//' *

Publishng a new version of the package:

    python3 setup.py sdist bdist_wheel
    twine upload dist/*
