===========
Mass Table
===========

Mass Table provides utilities to work with nuclear mass tables. At the moment the following tables are supported:


Examples:
  from 
    Table('DUZU').error(relative_to='AME2003')

    from towelstuff import location
    from towelstuff import utils

    if utils.has_towel():
        print "Your towel is located:", location.where_is_my_towel()

(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


Install
--------

Just do:

	pip install mass_table


Requirements
-------------
	
* python >= 2.7
* pandas >= 0.11
