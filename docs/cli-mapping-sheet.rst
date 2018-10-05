Command line tool - mapping-sheet option
========================================

This takes a schema and produces a spreadsheet with all field paths.

.. code-block:: shell-session

    bodskit mapping-sheet ~/work/openownership-data-standard/schema/person-statement.json > out.csv


This produces output like (truncated):

.. code-block:: csv

    section,path,title,description,type,range,values,links,deprecated,deprecationNotes
    ,addresses,Addresses,One or more addresses for this entity.,array,0..n,,,,
    ,addresses,Address,"A free text address string, providing as much address data as is relevant, suitable for processing using address parsing algorithms. For some uses (for example, Place of Birth) only a town and country are required.",object,,,,,
    addresses,addresses/address,Address,"The address, with each line or component of the address separated by a line-break or comma. This field may also include the postal code. ",string,1..1,,,,
    addresses,addresses/country,Country,The ISO 2-Digit county code for this address.,string,1..1,,,,
    addresses,addresses/postCode,Postcode,The postal code for this address.,string,1..1,,,,
    addresses,addresses/type,Type,What type of address is this?,string,1..1,"Codelist: placeOfBirth, home, residence, registered, service, alternative",,,

