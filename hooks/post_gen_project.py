{% if cookiecutter.use_pypi_deployment_with_travis == 'y' -%}
# After you create the Github repo and add it to Travis, run the
# travis_pypi_setup.py script to finish PyPI deployment setup
deploy:
  provider: pypi
  distributions: sdist bdist_wheel
  user: {{ cookiecutter.pypi_username }}
  password:
    secure: PLEASE_REPLACE_ME
  on:
    tags: true
    repo: {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    condition: $TOXENV == py27
{%- endif %}