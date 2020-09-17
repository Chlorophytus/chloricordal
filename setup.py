# Loosely based off https://github.com/pypa/sampleproject
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chloricordal',
    version='0.1.3',
    description='Yet another Discord bot for Python 3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Chlorophytus/chloricordal',
    packages=find_packages(),
)
