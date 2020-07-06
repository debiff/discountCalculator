# Mirta Backend Challange - Discount Calculator
Tool that calculates the applicable discount given a list of discount bundle, a list of product and the products in the cart

## Requirements

- [x] Python ^3.7
- [x] Poetry
- [x] Click

## Installation
First of all if you don't have done yet install [poetry](https://github.com/python-poetry/poetry).

```bash
pip install --user poetry
```
Clone the repo

```bash
git clone git@github.com:debiff/discountCalculator.git
```

Use Poetry to install all the dependencies of the project in a fresh virtual environment.

```bash
cd discountCalculator
poetry install
```

Activate the virtualenv and install the package:
```bash
poetry shell
pip install --editable .
```

## Usage
To compute the discount run
```bash
discount_calculator --cart ABC
```
Options:
- **--cart(required)**: The products in the cart comma separated.
- **--bundle(optional)**: Location of JSON file containing the bundles
- **--products(optional)**: Location of JSON file containing the products


## Test
To run the test suite execute from the parent folder containing the file flattify.py and the file test_flattify_unittest.py

```bash
python -m unittest discover tests/
```