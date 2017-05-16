"""Custom Exceptions for AgilePoint"""
from __future__ import print_function

class MissingRequiredArg(Exception):
    """Exception for missing required argument."""
    def __init__(self, message):
        super(MissingRequiredArg, self).__init__(message)
        self.message = message
    def __repr__(self):
        print('Missing required argument: {0}'.format(self.message))

class InvalidArg(Exception):
    """Exception for argument that should not be there."""
    def __init__(self, message):
        super(InvalidArg, self).__init__(message)
        self.message = message
    def __repr__(self):
        print('Invalid argument: {0}'.format(self.message))
