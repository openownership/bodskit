Command line tool - all-codes option
====================================

This takes a directory of code list files and produces a spreadsheet with all code list options.

.. code-block:: shell-session

    bodskit all-codes ~/work/openownership-data-standard/schema/codelists > out.csv


This produces output like (truncated):

.. code-block:: csv

    codelist,code,title,description,technical note
    addressType,placeOfBirth,Place of birth,,
    addressType,home,Home address,,
    addressType,residence,Residential address,,
    addressType,registered,Registered address,,
    addressType,service,Service address,,
    addressType,alternative,Alternative address,,
    annotationMotivation,commenting,Commenting,"The description field provides contextual comments for a field, object or statement.",


