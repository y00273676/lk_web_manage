#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the tornado web server setting
"""
import os

REDIS = {
    'host': '10.9.45.52',
    'port': 6379,
    'db': 0
}

app_conf = {
    'allowips': [],
    'appkey': '6f9c625e6b9c11e3bb1b94de806d866',
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static')
}

session_conf - {
    'cookie_secret': "e346976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
    'session_secret': "4cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
    'session_timeout': 1200,
    'store_options': REDIS
}
