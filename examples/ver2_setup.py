# coding: utf-8

from setuptools import setup, find_packages

NAME = "tes_server"
VERSION = \
    "0.0.6"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["nothing"]

setup(
    name=NAME,
    version=VERSION,
    description="REPY",
    author_email="",
    url="",
    keywords=["Swagger", "REPY"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['repy=repy.__main__:main']},
    long_description="""\
    This is a repy bla service
    """
)
