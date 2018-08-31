from setuptools import setup, find_packages
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jdcloud_sdk',
    version="1.2.12",
    description=long_description,
    author='JDCloud API Gateway Team',
    url='https://github.com/jdcloud-api/jdcloud-sdk-python',
    scripts=[],
    packages=find_packages(),
    install_requires=['requests'],
    license="Apache License V2.0"
)
