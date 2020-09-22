\:warning: **The Nimbus infrastructure project is no longer under development.** :warning:

For more information, please read the `news announcement <http://www.nimbusproject.org/news/#440>`_. If you are interested in providing IaaS capabilities to the scientific community, see `CHI-in-a-Box <https://github.com/chameleoncloud/chi-in-a-box>`_, a packaging of the `Chameleon testbed <https://www.chameleoncloud.org>`_, which has been in development since 2014.

----

====================================
Nimboss: The Nimbus Provisioning API
====================================

Install
=======

Create a virtualenv:
    $ virtualenv nimboss_env

Install the latest package from ooici:
    $ source nimboss_env/bin/activate
    $ easy_install --find-links http://ooici.net/packages/ nimboss


Developer Install
=================

Create a virtualenv::
    $ virtualenv nimboss_env

Install dependencies::
    $ pip -E nimboss_env install zope.interface httplib2 simplejson
    $ cd nimboss_env
    $ git clone git://github.com/apache/libcloud.git
    $ cd libcloud; python setup.py install; cd ..

Install Nimboss::
    $ git clone git@github.com:clemesha-ooi/nimboss.git # Read+Write, or use "git://...".
    $ cd nimboss
    $ python setup.py install


Tests
=====

Nimboss currently uses Python's unittest framework.

To run tests::
    $ cd tests
    $ python tests.py




Layout of Nimboss
=================

node.py
-------
Node specific connection and management.

cluster.py
----------
Cluster management and driver implementation for both EC2 and Nimbus.
Support for Cluster creation, termination, and status querying.

broker.py
---------
Communication with the Nimbus Context Broker.
Support for creating Context and querying Cluster status.

nimbus.py
---------
Nimbus 'Cluster document' and 'Cluster spec' utitlities.

