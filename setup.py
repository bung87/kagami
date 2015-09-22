#!/usr/bin/env python

from setuptools import setup, find_packages
import os

version = '0.1.1'

setup(
    name='kagami',
    version=version,
    description='Programmer tools with Chinese features',
    author='bung',
    author_email='zh.bung@gmail.com',
    license='MIT',
    keywords=['android sdk manager', 'maven', 'pypi', 'gem','bundle','npm','command line', 'cli'],
    url='https://github.com/bung87/kagami',
    packages=['kagami'],
    package_dir={'kagami': 'kagami'},
    package_data={
        'kagami': ['*.zip']
    },
    install_requires=[
        'PyYAML',
        'six'
    ],
    entry_points={
        'console_scripts': [
            'kagami=kagami.kagami:main'
        ],
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)