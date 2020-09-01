__version__ = "0.0.1"

try:
    import oreoweb
except ImportError:
    __oreoweb_version__ = None
else:
    __oreoweb_version__ = oreoweb.__version__
