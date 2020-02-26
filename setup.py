from setuptools import setup, find_packages

setup(
name='doge',
version='0.1',
packages=find_packages(exclude=['tests*']),
license='MIT',
description='example python package',
long_description=open('README.md').read(),
install_requires=['turtle', 'time'],
url='https://github.com/jo-moon/fluff',
author='Joanne Moonsamy',
author_email='joanne.moonsamy@gmail.com'
)
