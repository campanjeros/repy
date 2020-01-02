# coding: utf-8

from setuptools import setup

NAME = "repy"
VERSION = "0.3.2"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


setup(
    name=NAME,
    version=VERSION,
    description="Python release tagging tool",
    author_email="",
    url="",
    keywords=["repy"],
    scripts=['./repy']
)
