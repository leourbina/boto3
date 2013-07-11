class BotoException(Exception):
    """
    A base exception class for all Boto-related exceptions.
    """
    pass


class ServiceNotFound(BotoException):
    pass


class NoSuchObject(BotoException):
    pass
