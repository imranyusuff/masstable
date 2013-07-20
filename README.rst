===========
Nuclear Mass Table Toolkit
===========

The Nuclear Mass Table Toolkit provides utilities to work with nuclear mass tables. At the moment the following tables are supported:

	>>> Table().names
	'AME2003', 'AME2012', 'DUZU', 'FRDM95', 'KTUY05', 'ETFSI12', 'HFB14'

Examples:
---------

* Print first 5 elements from Audi 2003:

	>>> from masstable import Table
	>>> Table('AME2003').head()
	Z  N
	0  1     8.07132
	1  0     7.28897
	   1    13.13570
	   2    14.94980
	   3    25.90150


* Calculate the root mean squared error of Moller, et al.
Atomic Data and Nuclear Data Tables, 59(1995), 185-351.

	>>> Table('FRDM95').rmse(relative_to='AME2003')
	0.890859326191

* Calculate 2 neutron separation energies for even-even nuclei:

	>>> table = Table('AME2012').even_even.s2n
	Z  N 
	2  2           NaN
	   4      0.975454
	   6      2.125034
	   8     -1.417666
	4  2           NaN
	       ...

* Select nuclei with Z,N > 28:

	>>> condition = lambda Z,N: Z > 28 and N > 28
	>>> table.select(condition)
	30  30    28.016334
	    32    23.136434
	    34    20.978934
	    36    19.037934
	    38    17.250334
	    40    15.700534
	       ...

* Plot binding energies per nucleon:
	>>>
	>>> (t.binding_energy/t.A).plot()


Install
--------

Just do:

	pip install mass_table


Requirements
-------------
	
* python >= 2.7
* pandas >= 0.11
