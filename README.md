[![Build Status](https://travis-ci.org/elemental-analysis-group/elemental_analysis_tools.svg?branch=master)](https://travis-ci.org/elemental-analysis-group/elemental_analysis_tools)

![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/elemental-analysis-group/elemental_analysis_tools.svg) 
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/elemental-analysis-group/elemental_analysis_tools.svg)

![GitHub issues](https://img.shields.io/github/issues/elemental-analysis-group/elemental_analysis_tools.svg) 
![GitHub closed issues](https://img.shields.io/github/issues-closed/elemental-analysis-group/elemental_analysis_tools.svg)

Documentation:

  - [https://elemental_analysis_tools.readthedocs.io/](https://elemental_analysis_tools.readthedocs.io/)

## Instruction for a basic development setup:

Libraries instalation:

    virtualenv -p python3 .virtualenv
    source virtualenv/bin/activate
    pip3 install -r requirements.txt

Example of how to run tests, given you are at root directory:

    python3 tests/test_elementarDensity.py
    python3 tests/test_responseFactor.py
    python3 tests/test_winqxas.py
    python3 tests/test_blankCorrection.py
    python3 tests/test_micromatter.py
    python3 tests/test_shimadzu.py
    python3 tests/test_fitResponseFactor.py

Publishing a new version of the package in [pip](https://pypi.org/project/elemental-analysis-tools/):

    python3 setup.py sdist bdist_wheel
    pip3 install twine
    twine upload dist/*
