Geoconvert convert (obvious) data like zipcode, address, department name to generic data.

Support Python 2.6, 2.7, 3.3 and 3.4.

[![Build Status](https://travis-ci.org/jurismarches/geoconvert.svg?branch=master)](https://travis-ci.org/jurismarches/geoconvert)

Installation
============

Install the latest version from Github:

    $ pip install https://github.com/jurismarches/geoconvert/archive/master.zip

Examples
========

    from geoconvert.convert import zipcode_to_dept_name
    zipcode_to_dept_name('44300')
    'loire-altantique'

    from geoconvert.convert import address_to_zipcode
    address_to_zipcode('Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX')
    '33'

For more examples, take a look at unit tests.

Usage
=====

    from geoconvert.convert import zipcode_to_dept_name
    from geoconvert.convert import address_to_zipcode
    from geoconvert.convert import dept_name_to_zipcode
    from geoconvert.convert import region_id_to_name
    from geoconvert.convert import region_name_to_id
    from geoconvert.convert import country_name_to_id

Tests
=====

    python test_geoconvert.py

Releases
========

To release a new version you must update `__version__` on `geoconvert/__init__.py`
and tag the master branch with the same version.
