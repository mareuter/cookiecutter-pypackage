#!/usr/bin/env python

import os
import subprocess as sp

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_renovate }}' != 'y':
        remove_file('renovate.json')

    # Since setuptools_scm is used, this needs to get done.
    sp.run(["git", "init"])