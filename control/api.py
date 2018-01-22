#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API module
if need other operation befor save to db
add code in APICtrl
if not __getattr__ will use orm api
"""
class APICtrl(object):
    """
    you can add code to deal with the data
    __getattr__ will  use orm api
    """

    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.api = ctrl.pdb.api

    def __getattr__(self, name):
        return getattr(self.api, name)


