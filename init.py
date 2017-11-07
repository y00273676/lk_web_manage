#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lk_web_manage is a comprehensive web server
the git addrees :
"""
__author__ = 'yangguang'

#imports
import logging
import re
from tornado import web, httpserver, ioloop
from tornado.options import define, options, parse_command_line
from modules import UI_MODULES
from setting import app_conf, session_conf
from lib.session_manage import SessionManager
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#tornado defines
define('port', default=8787, help='listen port')
define('debug', default=True, help='debug mode')
define('log_to_stderr', default=True, help='')
define('log_file_max_size', default=1024, help='')
define('cookie_secret', type=str, default='lk_web_manage!@#', help='signing key for secrue cookies')
define('cache', default=True, help='enable memcached mode')

parse_command_line()

#web server  route
URLS = [
    (r'.*',
    (),
    )
]

def Application(web.Application):
    def __init__():
        self.logger = logging.getLogger(__name__)
        settings = {
            'debug': options.debug,
            'gzip': True,
            'static_path': app_conf['static_path'],
            'template_path': app_conf['template_path'],
            'cookie_secret': options.cookie_secret,
            'ui_modules': UI_MODULES
        }
        self.conf = app_conf
        self.session_manager = SessionManager(session_conf["session_secret"],
                session_conf["store_options"], session_conf["session_timeout"])
        tornado.web.Application.__init__(self, **settings)
        for spec in URLS:
            host = spec[0]
            patterns = spec[0][1:]
            self.add_handlers(host, patterns)

#start server
if __name__ == '__main__':
    app = Application()
    sock = tornado.netutil.bind_sockets(options.port)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sock)
    tornado.ioloop.IOLoop.current().start()
    logging.info('Exit')
