import re
import sys
import json
import requests
from urlparse import urljoin


def seq_iter(obj):
    if isinstance(obj, dict):
        return obj.iteritems()
    else:
        return enumerate(obj)


def transform_dict_or_list(d, f):
    for k, v in seq_iter(d):
        if isinstance(v, dict) or isinstance(v, list):
            v = transform_dict_or_list(v, f)
        d[k] = f(v)
    return f(d)


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def make_dotdict(d):
    if isinstance(d, dict):
        return dotdict(d)
    else:
        return d


class Purest(requests.Session):

    def __init__(self, base_url, transform_dict=True):
        super(Purest, self).__init__()
        self.__base_url = base_url
        self._transform_dict = transform_dict

    def request(self, method, url, **kwargs):
        url = urljoin(self.__base_url, str(url))
        response = super(Purest, self).request(method, url, **kwargs)
        result = response.json()
        if self._transform_dict:
            return transform_dict_or_list(result, make_dotdict)
        else:
            return result

    def __getattr__(self, name):
        url = urljoin(self.__base_url, name + '/')
        return Purest(url)

    def __getitem__(self, name):
        url = urljoin(self.__base_url, str(name) + '/')
        return Purest(url)

    def __call__(self, *args, **kwargs):
        return self.get(self.__base_url)


class RESTImporter(object):

    def find_module(self, fullname, path=None):
        if fullname.startswith('purest'):
            return self
        else:
            return None

    def load_module(self, name):
        urlName = name.split('.')[1]
        urlNew = urlName.replace('_', '.')
        url = "https://" + urlNew.lower()

        return Purest(url)

sys.meta_path = [RESTImporter()]
