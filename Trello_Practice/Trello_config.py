from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth, HTTPDigestAuth


# class
class RestAPIConfig:
    TIME_OUT_DURATION = 10


# Constructor -- passing instant Variables
def __init__(self):
    self.baseurl = None
    self.endpoint = None
    self.content_type = None
    self.accept_type = None
    self.headers = {}
    self.auth = None
    self.param = None
    self.allow_redirects = False
    self.time_out = RestAPIConfig.TIME_OUT_DURATION


def include_header(self, key, value):
    self.headers = CaseInsensitiveDict()
    self.headers[key] = value


def include_accept(self, value):
    self.headers = CaseInsensitiveDict()
    self.headers['Accept'] = value


def include_content_type(self, value):
    self.headers = CaseInsensitiveDict()
    self.headers['Content_Type'] = value


def include_basic_authentication(self, username, password):
    self.auth = HTTPBasicAuth(username, password)


def include_digest_authentication(self, username, password):
    self.auth = HTTPDigestAuth(username, password)
