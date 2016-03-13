__author__ = 'Administrator'

from handlers.index import *

from handlers.auth import *
urls = [
    (r'/',MainHandler),
    (r'/login', LoginHandler),

]

urls += [
    (r'/love',LoveHandler),
]