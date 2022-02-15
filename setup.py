# coding=utf-8


from curses import use_env
from setuptools import setup

setup(name='py-digits',
      version='0.1.6',
      description='Sum the first X Pi digits',
      url='https://github.com/Baelfire18/pi-digits',
      author='Jose Antonio Castro',
      long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
      long_description_content_type= 'text/markdown',
      author_email='jacastro18@uc.cl',
      license='MIT',
      packages=['pydigits'],
      install_requirements=open('requirements.txt').read().splitlines(),
      keywords=['pi', 'sum', 'CAPTCHA', 'robot', 'binary'],
      zip_safe=False,
      use_scm_version=True,
      setup_requires=['setuptools_scm']
      )
