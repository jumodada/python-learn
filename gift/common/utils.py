# coding:utf-8

import os
import time

from .error import NotPathError, FormatError, NotPathError


def timestamp_to_string(timestamp):
    time_obj = time.localtime(timestamp)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
    return time_str


def check_file(path):
    if not os.path.exists(path):
        raise NotPathError('not found %s' % path)

    if not path.endswith('.json'):
        raise FormatError('need json format')

    if not os.path.isfile(path):
        raise NotPathError('this is a not file')
