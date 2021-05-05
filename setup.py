"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup
setup(
    name='lambdatabrennanashley',  # Required
    version='0.0.1',  # Required
    author='brennanashley',  # Optional
    author_email='ashley-brennan@lambdastudents.com',  # Optional
    keywords='functions',  # Optional
    packages=['mymodule'],  # Required
    python_requires='>=3.6, <4',
)