from distutils.core import setup

setup(
    name='MassTable',
    version='0.1.0',
    author='Yaser Martinez',
    author_email='yaser.martinez@gmail.com',
    packages=['masstable'],
    url='http://pypi.python.org/pypi/masstable/',
    license='LICENSE.txt',
    description='Utilities for working with nuclear mass tables.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pandas >= 0.11.0"
    ],
)