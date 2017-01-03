#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import simplejson as json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default = 8000, help = "run on the given port", type = int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('./mock.json')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers = [(r'/', IndexHandler)],
                                  debug = True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
