# Py digits

[![lint][lint-image]][lint-url]

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

## Testing

Run the test suite with:

```sh
python -m unittest tests
```

To install it locally from the source code:

```sh
python setup.py develop
```

## Publish

```sh
python setup.py register sdist upload
```

[lint-image]: https://codeclimate.com/github/Baelfire18/py-digits/badges/gpa.svg
[lint-url]: https://codeclimate.com/github/Baelfire18/py-digits
