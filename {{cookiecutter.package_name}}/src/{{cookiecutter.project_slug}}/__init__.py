__all__ = [
    "__author__",
    "__email__",
    "__version__",
    "version_info",
]

from importlib.metadata import PackageNotFoundError, version

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'

try:
    __version__ = version("{{ cookiecutter.project_slug }}")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"

version_info = __version__.split(".")
"""The decomposed version, split across "``.``."

Use this for version comparison.
"""