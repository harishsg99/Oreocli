from . import formatutils as fmt
from .version import __oreoweb_version__, __version__

DOCS = "https://oreowebweb.github.io"
VERSION = __version__
oreoweb_VERSION = (
    fmt.muted("[not installed]")
    if __oreoweb_version__ is None
    else fmt.version(__oreoweb_version__)
)
