<p align="center">
    <img src="https://raw.githubusercontent.com/anatolereffet/prioritealist/master/docs/source/sand_logo_lightmode.png" style="transform: scale(0.5);>
</p>

<h2 align="center">Priori-Tea List: Sipping Success One Task at a Time</h2>

<p align="center">
  <a href="https://github.com/anatolereffet/prioritealist/actions"><img alt="Actions Status" src="https://github.com/anatolereffet/prioritealist/workflows/Semantic Release/badge.svg"></a>
  <a href="https://pypi.org/project/prioritealist/"><img alt="PyPI" src="https://img.shields.io/pypi/v/prioritealist"/></a>
  <img src="https://badgen.net/pypi/python/prioritealist" />
  <a href="https://github.com/anatolereffet/prioritealist/blob/master/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/anatolereffet/prioritealist"/></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/></a>
</p>

## Booting up the environment

In the root project folder
```bash
pip install poetry
```

```bash
poetry init
poetry add prioritealist
```

To create your poetry environment
```bash
poetry shell
```
To deactivate the environment
```bash
deactivate
```
To run the different tests/type hints, use the makefile such as 
```bash
make lint
```
The various commands can be seen in the Makefile