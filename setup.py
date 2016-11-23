# -*- coding: utf-8 -*-

from setuptools import setup


def get_long_description():
    with open('README.md') as f:
        rv = f.read()
    return rv


def get_requirements():
    with open('requirements/prod.txt') as f:
        rv = f.read().splitlines()
    return rv

setup(
    name='puREST',
    packages=['purest'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    version='0.0.2',
    description='Simple dynamic REST consumer',
    long_description=get_long_description(),
    install_requires=get_requirements(),
    author='Michal Vlasák',
    author_email='daeatel@gmail.com',
    url='https://github.com/vlasy/purest',
    license='MIT'
)
