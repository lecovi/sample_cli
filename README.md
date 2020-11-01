# Sample Python CLI

Sample repository for creating a CLI in Python.

## Motivation

This repository is for educational purposes. I want to show how to create an executable 
CLI tool written in Python. With this I wanna cover:

- [ ] Creating a Python Package using traditional `setup.py`.
- [ ] Creating a Python Package using `poetry`.
- [ ] Publishing to PyPI.
- [ ] Creating a simple CLI tool that installs on to your system and is executable.
- [ ] Creating plugins for the CLI tool that are *pipinstalable*.

# Package

We are going to create a package called `pier-mob`. Why? Just because! I don't wanna use
traditional `example`, `foo`, or `bar` because I think those names lack semantics
and the use of such names becomes difficult for less experienced devs to understand. If
you are wondering, I let [roke](https://github.com/ralsina/roke) choose the name for the 
example tool that we are going to build.

Add files and directories:

```baah
pier_mob
|-- LICENSE               # License file
|-- README.md             # **This** file
|-- pier_mob              # Main directory: all source code inside
|   |-- __init__.py       # needed for converting directory into a package
|   |-- __main__.py       # Defines what is executed when package is called
|   `-- cli.py            # Sample source code module
|-- setup.py              # Python Packaging config file
`-- tests                 # Test cases directory
    |-- __init__.py       # needed for converting directory into a package
    `-- test_version.py   # Test source code sample
```

With this minimal structure we can run our program as module and as a simple script.
Using [pip](https://github.com/pypa/pip/blob/master/src/pip/__main__.py) strategy to be
able of running in both ways. Look deeper on [`pier_mob/__main__.py`](./pier_mob/__main__.py).

As simple script:

```bash
$ python3 pier_mob
Pier Mob v0.0.1
```

And running as module:

```bash
$ python3 -m pier_mob
Pier Mob v0.0.1
```

Also with this minimal structure we have tests.

Tests can be run as:

```bash
$ python3 setup.py tests
```


# Resources

- [Packaging Python](https://packaging.python.org/tutorials/packaging-projects/)
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/index.html)
