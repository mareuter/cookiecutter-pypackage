======================
cookiecutter-pypackage
======================

Cookiecutter template for a Python package. See https://github.com/mareuter/cookiecutter.

* Free software: BSD license
* Uses a tests directory
* Uses pyproject.toml
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Travis-CI_: Ready for Travis Continuous integration testing and version deployment
* Tox_ testing: Setup to easily test for python
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Wheel_ support: Use the newest python package distribution standard from the get go

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/mareuter/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run `tox` to make sure all tests pass.
* Release your package the standard Python way.

This repository was originally forked from this one and inspired by it.

* `Nekroze/cookiecutter-pypackage`_: This repo was fork from here.

.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _Pytest: http://pytest.org/
.. _Wheel: http://pythonwheels.com
