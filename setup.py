# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rest_test
version = rest_test.__version__

setup(
    name='rest_test',
    version=version,
    author='',
    author_email='vikrant.pogula@gmail.com',
    packages=[
        'rest_test',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['rest_test/manage.py'],
)