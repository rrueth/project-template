An Initial Python Project Template
==================================

This repo is designed to be a baseline for creating a successful python project including:
- Setting up a common dev environment.
- Defining common commands (e.g. setup virtualenv, build, run tests, etc.).
- Testing on all supported client versions.
- Setting up continuous integration.
- Deploying to PyPI.

Project website: https://github.com/rrueth/python-project-template

The Tools
=========

Vagrant
-------

Vagrant is used to create a common development environment for all users. The Vagrantfile_ and `bootstrap.sh`_ file will
install all of the packages necessary to run and interact with everything in this project template.

To get up and running with vagrant:
- Install vagrant: https://www.vagrantup.com/docs/installation/
- Install VirtualBox: https://www.virtualbox.org/wiki/Downloads

To get started::

	vagrant up
	vagrant ssh
	cd /vagrant

.. Tip::
	If you're running Vagrant on Windows, make sure to always open up your shell as an administrator. Otherwise,
	Vagrant may have difficulties working with symlinks.

Travis CI
---------

For open source projects on GitHub, Travi CI is to go for running continuous integration. Travis supports easily testing
against multiple Python versions and easily publishing to PyPI_ through a simple `.travis.yml`_ file.

Travis References
~~~~~~~~~~~~~~~~~

- Getting started guide

	- https://docs.travis-ci.com/user/getting-started/

- Use Travis CI to deploy to PyPI

	- https://docs.travis-ci.com/user/deployment/pypi

Virtualenv
----------

Virtualenv_ is a tool for creating isolated Python environments so that you can install whichever dependencies and
versions you need without worry about messing up your system libraries/dependencies.

tox
---

tox_ is a Python tool that makes it easy to test your package against multiple versions of Python (including
installation and testing). tox_ uses a simple `tox.ini`_ configuration file to specify which versions of Python to test
against.

Pylint
------

Pylint_ is a code analysis tool that identifies Python error, mistakes, and code style infringements. To decide what to
check, Pylint_ uses a comprehensive `.pylintrc`_ configuration file.

Package Structure
=================
::

	- .gitignore
	- .pylintrc
	- .travis.yml
	- bootstrap.sh
	- LICENSE
	- Makefile
	- README.rst
	- requirements.txt
	- setup.py
	- tox.ini
	- Vagrantfile
	- <package_name>/
		- __init__.py
		- *.py
		- tests/
			- __init__.py
			- *_test.py

.gitignore
----------

A standard .gitignore file that ignores common files.

.. _`.pylintrc`:

.pylintrc
---------

An aggressive Pylint configuration that attempts to run most useful Pylint checks. For a full list of all available
Pylint_ checks, see https://docs.pylint.org/features.html.

.. _`.travis.yml`:

.travis.yml
-----------

The Travis-CI configuration file specifies to run the continuous integration server against all supported versions of
Python. Additionally, if you plan to deploy to PyPI_, it is highly recommended to use Travis-CI to deploy to PyPI_ when
also pushing a git tag.

.. _`.bootstrap.sh`:

bootstrap.sh
------------

Used by Vagrant_ and the Vagrantfile_ to install all of the necessary packages when starting a new virtual machine.

LICENSE
-------

By default, this project uses the `MIT License`_. The MIT License is a very basic and permissive license that enables
the user use and modify the package without imposing many restrictions. For a good reference on other licenses that are
available, see http://choosealicense.com/.

Makefile
--------

A default Makefile for building, linting, testing, and cleaning

README.rst
----------

A general README file explaining anything that you want your users to know about your package. PyPI_ requires the README
to be written in ReStructedText, and Github is capable of using either Markdown or ReStructuredText. Since
ReStructuredText is supported by Github and PyPI_, it is the recommend syntax for the README.

RestructuredText Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~

- A quick primer: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
- A quick reference guide: http://docutils.sourceforge.net/docs/user/rst/quickref.html
- An extensive reference guide: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
- An online tool for testing and rendering ReStructuredText: http://rst.ninjs.org/

requirements.txt
----------------

The industry standard mechanism to define dependencies for pip_. By default, this template includes packages to run lint
and build and run unittests.

setup.py
--------

``setup.py`` is the standard mechanism for creating a Python package. For more details about ``setup.py``, see
https://packaging.python.org/en/latest/distributing/#initial-files.

.. _`tox.ini`:

tox.ini
-------

The tox_ configuration file only specifies how to run the unittests and to test against all supported versions of
Python.

.. _Vagrantfile:

Vagrantfile
-----------

The configuration file for Vagrant_ defines which operating system to use and how to install all of the required
packages.

Tests Directory
---------------

The tests directory is included inside the package in order for the tests to live as close to the code as possible. The
tests are in their own directory so that we can easily exclude them from your package in setup.py.  The tests directory
contains an ``__init__.py`` file so that Pylint is able to discover the test files.

.. _`MIT License`: http://choosealicense.com/licenses/mit/
.. _pip: https://pip.pypa.io/en/stable
.. _Pylint: https://docs.pylint.org/
.. _PyPI: https://pypi.python.org/pypi
.. _tox: https://testrun.org/tox/latest/
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/