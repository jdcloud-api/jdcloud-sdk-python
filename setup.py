from setuptools import setup, find_packages
from jdcloud_sdk.core.version import version

setup(
    name='jdcloud_sdk',
    version=version,
    description='JDCloud SDK for Python',
    author='JDCloud API Gateway Team',
    url='',
    scripts=[],
    packages=find_packages(exclude=['demo']),
    install_requires=['requests'],
    license="Apache License V2.0"
)
