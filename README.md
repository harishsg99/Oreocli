# oreoweb CLI [![Join the chat at https://gitter.im/Oreoweb/community](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Oreoweb/community) ![test](https://forthebadge.com/images/badges/made-with-python.svg)


[pypi-url]: https://pypi.org/project/oreoweb-cli

oreoweb CLI provides standard development tooling for [oreoweb].

[oreoweb]: https://github.com/harishsg99/oreoweb

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
