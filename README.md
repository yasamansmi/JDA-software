# jda Software

A package to forecast the rented bikes per hour!

## Installation

For installation please first install [Poetry](https://python-poetry.org/docs/). Then make a virtual evironment using poetry.

```sh
poetry install
```

In order to acitivate the built virtual environment, run the following command.

```sh
poetry shell
```

The jupyter notebook can be then loaded after running poetry shell command and should work on the poetry built kerenl.

```sh
python -m 
jupyter notebook
```

## Tests

The tests are not completer for this package and are just written as sample. In order to run the unit tests, run the following commands:

```sh
cd tests
pytest test_preprocessing.py
pytest test_randomforest.py
```

## Documentation

In order to make the documentation you can refer to the doc directry by:

```sh
cd src/doc/build/html
firefox index.html
```

Or alternatively open the index.html with a browser.

After a change in the code you can make the document again usig sphinx by tunning the following commands:

```sh
cd src/doc/
make html
```

## Quick Run

To Run the a predetermined version of the algorithm and observe sample obeservations for a sample data, run the following:

```sh
src/main.py
```

## Run Jupyter notebook

You can run and instance of jupyter notebook which gives you a higher level of control over the attributes and hyperparameters. Please run the follwing commands after installing the virtaul environments. 

```sh
poetry shell
pip install ipykernel
pip install jupyter
cd utils
jupyter notebook
```

Plese open Package_Test.ipynb and test the model using the existing prototype.

