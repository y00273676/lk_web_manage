#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tornado UIModule
PageModule: web server page info
"""
from tornado import web


 class PageModule(web.UIModule):
     """
     add page info
     """
     def render(self, page, page_total, base_url, max_display=20):
        return self.render_string('ui-mod/page-module.tpl',
            page=page,
            page_total=page_total,
            base_url=base_url,
            max_display=max_display)


