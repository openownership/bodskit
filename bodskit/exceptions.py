class BODSKitError(Exception):
    """Base class for exceptions from within this package"""


class CommandError(BODSKitError):
    """Errors from within this package's CLI"""
