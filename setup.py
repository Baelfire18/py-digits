# coding=utf-8


from setuptools import setup

setup(name='pi-digits',
      version='0.1.0',
      description='Sum the first X Pi digits',
      url='https://github.com/Baelfire18/pi-digits',
      author='Jose Antonio Castro',
      long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
      long_description_content_type= 'text/markdown',
      author_email='jacastro18@uc.cl',
      license='MIT',
      packages=['pidigits'],
      install_requirements=open('requirements.txt').read().splitlines(),
      keywords=['pi', 'sum', 'CAPTCHA', 'robot', 'binary'],
      zip_safe=False)
