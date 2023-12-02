install:
  poetry install --with lint

test:
  pytest

clean:
  rm -fr build/
  rm -fr .eggs/
  find . -name '*.egg-info' -exec rm -fr {} +
  find . -name '*.egg' -exec rm -f {} +
  find . -name '*.pyc' -exec rm -f {} +
  find . -name '*.pyo' -exec rm -f {} +
  find . -name '*~' -exec rm -f {} +
  find . -name '__pycache__' -exec rm -fr {} +
  rm -fr .coverage
  rm -fr coverage.xml
  rm -fr coverage.json
  rm -fr htmlcov/
  rm -fr .pytest_cache
  rm -fr .mypy_cache
