from setuptools import setup, find_packages

setup(
    name='masstable',
    version='0.1.1',
    author='Yaser Martinez',
    author_email='yaser.martinez@gmail.com',
    packages=find_packages(),
    url='https://github.com/elyase/masstable',
    license='LICENSE.txt',
    description='Utilities for working with nuclear mass tables.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pandas >= 0.11.0"
    ],
)