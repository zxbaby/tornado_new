__author__ = 'Administrator'

from base import BaseHandler

import tornado.escape


class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect('/login')
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render('index.html',name=name)




class LoveHandler(BaseHandler):
    def get(self):
        self.render('love.html')
