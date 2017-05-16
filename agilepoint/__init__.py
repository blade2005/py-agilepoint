"""AgilePoint API Lib"""
import requests
from hammock import Hammock
from .admin import Admin
from .workflow import Workflow

# pylint: disable=too-few-public-methods

class AgilePoint(object):
    """AgilePoint API"""
    def __init__(self, host, path, username, password):
        url = '{}/{}'.format(host, path)
        self.agilepoint = Hammock(url, auth=(username, password))
        self.workflow = Workflow(self.agilepoint)
        self.admin = Admin(self.agilepoint)
