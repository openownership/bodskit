Command line tool - schema-codelist-report option
=================================================


Reports details of a JSON Schema (open and closed codelists).

.. code-block:: shell-session

    bodskit schema-codelist-report ~/work/openownership-data-standard/schema/person-statement.json


This produces output like:

.. code-block:: csv

    codelist,type
    addressType.csv,Closed
    annotationMotivation.csv,Open
    nameType.csv,Closed
    personType.csv,Closed
    sourceType.csv,Closed
    statementType.csv,Closed

