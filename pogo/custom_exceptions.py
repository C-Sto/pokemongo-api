class GeneralPogoException(Exception):
    """Throw an exception that moves up to the start, and reboots"""


#  todo: don't do it like this
class NoBallException(Exception):
    """Throw an exception that isn't so bad"""

class PogoResponseException(GeneralPogoException):
    """Throw an exception at bad responses"""
