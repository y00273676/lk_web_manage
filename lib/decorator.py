#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tools for orm
"""
import functools
from sqlalchemy.orm import class_mapper
from functools import wraps
import pickle
import logging


def model2dict(model):
    """
    convert item to dict
    """
    if not model:
        return {}
    fields = class_mapper(model.__class__).columns.keys()
    return dict((col, getattr(model, col)) for col in fields)

def model_to_dict(func):
    """
    wrap tools for convert item to dict
    """
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return model2dict(ret)
    return wrap

def models_to_list(func):
    """
    convert item to list

    """
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return [model2dict(r) for r in ret]
    return wrap

def close_conn(name='master'):
    """
    use for orm
    close connection after commit
    """
    def outer(func):
        def inner(*arg, **kwargs):
            self = arg[0]
            ret = func(*arg, **kwargs)
            getattr(self, name).close()
            return ret
        return inner
    return outer

class DictProperty(object):
    """ Property that maps to a key in a local dict-like attribute. """

    def __init__(self, attr, key=None, read_only=False):
        self.attr, self.key, self.read_only = attr, key, read_only

    def __call__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter, self.key = func, self.key or func.__name__
        return self

    def __get__(self, obj, cls):
        if obj is None: return self
        key, storage = self.key, getattr(obj, self.attr)
        if key not in storage: storage[key] = self.getter(obj)
        return storage[key]

    def __set__(self, obj, value):
        if self.read_only: raise AttributeError("Read-Only property.")
        getattr(obj, self.attr)[self.key] = value

    def __delete__(self, obj):
        if self.read_only: raise AttributeError("Read-Only property.")
        del getattr(obj, self.attr)[self.key]


