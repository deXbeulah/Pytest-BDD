# Pytest-BDD
Behaviour Driven Development using Pytest.

## Third Party Packages used
 - pytest
 - pytest-cov
 - pytest-html
 - requests

 To install each package, enter ```pip install <package-name>``` on the terminal. e.g ```pip install pytest```.

## Running Tests
Using ```cd```, change into the folder where you have your python test script on the terminal and run the following command.```python -m pytest```

## Pytest Commands and Configs
```python -m pytest --verbose``` - Pytest prints more info(including: cachdir, metadata, rootdir, plugins) and a status(Pass or Fail) report, and failure intropection for each test when run.

```python -m pytest --quiet``` - Pytest prints only the 'dot's, 'F's and the intropecture report.

```python -m pytest --exitfirst``` - Pytest exit as soon as the first failure happens. 

```python -m pytest --maxfail=<Number of failures>``` - Exit test after the number of failure specified in <Number offailures>.

## Pytest Plugins
Pytest html - install: ```pip install pytest-html``` To run: ```python -m pytest --html=<path to html file>```

Pytest code coverage - install: ```pip install pytest-cov``` To run: ```python -m pytest --cov=<test module>```

Pytest xdist - install: ```pip install pytest-xdist``` To run: ```python -m pytest -n <number of dist to run```

Pytest Behaviour Driven Development(BDD) - install: ```pip install pytest-bdd``` To run: