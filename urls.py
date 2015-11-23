__author__ = 'Administrator'

from handlers.index import *

urls = [
    (r'/',MainHandler),
]

urls += [
    (r'/love',LoveHandler),
]