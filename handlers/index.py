__author__ = 'Administrator'

from base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')

class LoveHandler(BaseHandler):
    def get(self):
        self.render('love.html')
