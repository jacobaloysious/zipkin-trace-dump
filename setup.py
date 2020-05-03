# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ZipkinTraceDump',
    version='0.0.1',
    description='Package for Zipkin Trace DumpParser',
    long_description=readme,
    author='Jacob Aloysious',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
