# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = "totalcorner"

setup(
    name="totalcorner",
    version="0.1.0",
    description="totalcorner.com api client",
    license="MIT",
    author="jim zhou",
    packages=find_packages(),
    install_requires=['requests'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
