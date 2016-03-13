__author__ = 'Administrator'

from base import BaseHandler
<<<<<<< HEAD
import tornado.escape


class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect('/login')
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render('index.html',name=name)


=======

class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')
>>>>>>> 87319db5d0b5ee11cb1dcfe00c116d092b99fb95

class LoveHandler(BaseHandler):
    def get(self):
        self.render('love.html')
