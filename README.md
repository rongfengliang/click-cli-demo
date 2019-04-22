# simple cli demo project


## how to running

* init venv

```code
python3 -m venv .
```

* install click pacakge

* activate venv

```code
source bin/activate
```

* install click pacakge

```code
pip install click
```

* install with pip pacakge for test

```code
pip install .
```

* test cli

```code
dalongcli --name dalong --count 3
```

result

```code
Hello, dalong!
Hello, dalong!
Hello, dalong!
```

## publish to test pypip

> use venv 

* install dep pacakges

```code
python -m pip install --user --upgrade setuptools wheel --no-warn-script-location
```

* build dist files

```code
python3 setup.py sdist
```

* push

> you may register one account from [website](https://test.pypi.org)

```code
install twine  for push:

python3 -m pip install --user --upgrade twine

push command:
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
