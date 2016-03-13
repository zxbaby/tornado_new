__author__ = 'Administrator'

from handlers.index import *
<<<<<<< HEAD
from handlers.auth import *
urls = [
    (r'/',MainHandler),
    (r'/login', LoginHandler),
=======

urls = [
    (r'/',MainHandler),
>>>>>>> 87319db5d0b5ee11cb1dcfe00c116d092b99fb95
]

urls += [
    (r'/love',LoveHandler),
]