"""
Tests for `{{ cookiecutter.package_name }}` module.
"""
import pytest
from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name|capitalize }}


class Test{{ cookiecutter.package_name|capitalize }}:

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass
