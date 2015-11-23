__author__ = 'Administrator'
import os
import tornado.web
from urls import urls

settings = {
    "template_path": os.path.join(os.path.dirname(__file__),"templates"),
    "static_path": os.path.join(os.path.dirname(__file__),"static"),
    "debug": True,
    #"logging": "debug",
    "login_url": '/login',
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "xsrf_cookies": True,
}

application = tornado.web.Application(
    handlers = urls,
    **settings
)

PORT = 22222

DBINFO = dict(
    dbhost = '127.0.0.1',
    dbuser = 'root',
    dbpasswd = '',
    dbport = 3306,
    dbdatabase = 'devops'
)