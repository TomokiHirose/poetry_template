# poetry_template

Project template for Python development with Poetry.<br>
Please edit according to your environment.


## install 

```sh
$ poetry install
```

## update

```sh
$ poetry add xxx
$ poetry update
```

## Use Scripts
### Pytest
```sh
$ poetry run test
```

### Format
```sh
# black and isot work for template dirs
$ poetry run format
```

### Lint
```sh
# flake8 and mypy work for template dirs
$ poetry run lint
```

## CreateAPI Documents
```sh
$ poetry run apidoc
```

## CreateTest Documents
```sh
$ poetry run testdoc
```

## Compute Metrics
```sh
$ poetry run metrics
```

## Build(create wheel)
```sh
$ poetry build
```

## Create Git commit hook
```sh
$ poetry run pre-commit install
```
