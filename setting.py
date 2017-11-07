#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the tornado web server setting
"""
import os

app_conf = {
    'allowips': [],
    'appkey': '6f9c625e6b9c11e3bb1b94de806d866',
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static')
}
