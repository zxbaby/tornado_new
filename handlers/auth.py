__author__ = 'Administrator'
from base import *

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('checkflag', "true")
        self.render('login.html')

    def post(self, *args, **kwargs):
        if not self.request.headers.get('Cookie'):
            self.render('require_enable_cookie.html')
            return
        self.set_secure_cookie('user', self.get_argument('username'))
        self.redirect('/')