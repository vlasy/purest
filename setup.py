# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='puREST',
    packages=['purest'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    version='0.0.1',
    description='Simple dynamic REST consumer',
    author='Michal Vlasák',
    author_email='daeatel@gmail.com',
    url='https://github.com/vlasy/purest'
)
