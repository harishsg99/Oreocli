# oreoweb CLI (UNMAINTAINED)

[![pypi](https://img.shields.io/pypi/v/oreoweb-cli.svg)][pypi-url]
[![travis](https://img.shields.io/travis/oreowebproject/oreoweb-cli.svg)](https://travis-ci.org/oreowebproject/oreoweb)
[![black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/ambv/black)
[![codecov](https://codecov.io/gh/oreowebproject/oreoweb-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/oreowebproject/oreoweb-cli)
![license](https://img.shields.io/pypi/l/oreoweb-cli.svg)

[pypi-url]: https://pypi.org/project/oreoweb-cli

oreoweb CLI provides standard development tooling for [oreoweb].

[oreoweb]: https://github.com/oreowebproject/oreoweb

![](media/demo.gif)

## Install

```bash
pip install oreoweb-cli
```

## Usage

### Overview

```
$ oreoweb --help
Usage: oreoweb [OPTIONS] COMMAND [ARGS]...

Options:
  -V, --version  Show the version and exit.
  --help         Show this message and exit.

Commands:
  create  Initialize a oreoweb project.
```

### Create a project

```
$ oreoweb create --help
Usage: oreoweb create [OPTIONS] NAME

  Initialize a oreoweb project.

  Hint: use `-d .` to generate files in the current directory.

Options:
  -d, --directory DIRECTORY  Directory where the project should be created.
                             Created if does not exist. Defaults to `NAME`.
  --dry                      Do not write anything to disk.
  --no-input                 Send default answers to prompts.
  --help                     Show this message and exit.
```

## Contributing

Want to contribute code or documentation? Great to hear! Our [Contributing Guidelines](https://github.com/oreowebproject/oreoweb-cli/blob/master/CONTRIBUTING.md) are here to help.

## License

MIT
