# datasette-upgrade

[![PyPI](https://img.shields.io/pypi/v/datasette-upgrade.svg)](https://pypi.org/project/datasette-upgrade/)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-upgrade?include_prereleases&label=changelog)](https://github.com/datasette/datasette-upgrade/releases)
[![Tests](https://github.com/datasette/datasette-upgrade/workflows/Test/badge.svg)](https://github.com/datasette/datasette-upgrade/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-upgrade/blob/main/LICENSE)

Upgrade Datasette instance configuration to handle new features

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-upgrade
```
## Usage

**This plugin is in development and does not yet do anything useful.**

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-upgrade
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```