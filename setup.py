#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'aniso8601',
    'apipkg',
    'astroid',
    'atomicwrites',
    'attrs',
    'click',
    'coverage',
    'execnet',
    'Flask',
    'isort',
    'itsdangerous',
    'Jinja2',
    'lazy-object-proxy',
    'MarkupSafe',
    'mccabe',
    'mock',
    'more-itertools',
    'pathlib2',
    'pbr',
    'pep8',
    'pluggy',
    'py',
    'pymongo',
    'pytz',
    'six',
    'typed-ast',
    'Werkzeug',
    'wrapt',
    'uWSGI',
]

setup(
    name="report-service",
    author="Paulo Silva",
    author_email="paulosilvadev3@gmail.com",
    description="API - Reports to data of complains and companies",
    version="1.0",
    install_requires=requirements,
    extras_require={
        'dev':[
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'pytest-flask',
            'pytest-cache',
            'pytest',
            'pylint',
        ]
    }
)
