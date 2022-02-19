# Py digits

[![GitHub release](https://img.shields.io/github/v/release/Baelfire18/py-digits.svg)](../../releases/latest)
[![lint][lint-image]][lint-url]
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This library was inspired by this meme:

![Robot captcha meme](https://raw.githubusercontent.com/Baelfire18/py-digits/master/assets/Captcha.jpg)

Now we can easily solve it in less than a second!

## Getting started

Install the library with:

```sh
pip install -U py-digits
```

### Usage

```python
from pydigits import sum_pi_digits

print(sum_pi_digits(31_415, 'odd'))
# 78662

print(sum_pi_digits(31_415, 'odd', 'binary'))
# 10011001101000110
```

## Documentation

### pi_digits

```python
function pydigits.pi_digits(decimals)
```

Function that returns the `pi` number rounded to the number of digits given has an argument.

#### Parameters

+ decimals: `int`.
Number of digits of `pi` requested.

### sum_pi_digits

```python
function sum_pi_digits(decimals, nature="all", notation="decimal")
```

#### Parameters

+ decimals: `int`.
Number of digits of `pi` requested.

+ nature: `"all"`, `"even"` or `"odd"`, default `"all"`.
The nature of the digits of `pi` taht you want to count for your sum.

+ notation: `"decimal"` or `"binary"`, default `"decimal"`.
The notation of the answer obtained.

## Testing

Run the test suite with:

```sh
python -m unittest tests
```

## Install Local

To install it locally from the source code:

```sh
python setup.py develop
```

[lint-image]: https://codeclimate.com/github/Baelfire18/py-digits/badges/gpa.svg
[lint-url]: https://codeclimate.com/github/Baelfire18/py-digits
