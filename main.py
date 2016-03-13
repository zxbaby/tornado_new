__author__ = 'Administrator'

import os, sys, datetime
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from settings import settings, application, PORT

define('port', default=PORT, type=int, help='config the server run the port')

def main():
    tornado.options.parse_command_line()
    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()