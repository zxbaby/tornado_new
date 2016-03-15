__author__ = 'Administrator'
from base import *
import tornado.escape

# class LoginHandler(BaseHandler):
#     def get(self, *args, **kwargs):
#         self.set_cookie('checkflag', "true")
#         self.render('login.html')

#     def post(self, *args, **kwargs):
#         if not self.request.headers.get('Cookie'):
#             self.render('require_enable_cookie.html')
#             return
#         self.set_secure_cookie('user', self.get_argument('username'))
#         self.redirect('/')

class LoginHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        incorrect = self.get_secure_cookie("incorrect")
        if incorrect and int(incorrect) > 25:
            self.write('<center>blocked</center>')
            return
        self.render('login.html')

    @tornado.gen.coroutine
    def post(self):
        getusername = tornado.escape.xhtml_escape(self.get_argument("username"))
        getpassword = tornado.escape.xhtml_escape(self.get_argument("password"))
        if "demo" == getusername and "demo" == getpassword:
            self.set_secure_cookie("user", self.get_argument("username"))
            self.set_secure_cookie("incorrect", "0")
            # self.redirect(self.reverse_url("main"))
            self.redirect('/')
            
        else:
            incorrect = self.get_secure_cookie("incorrect")
            if not incorrect:
                incorrect = 0
            self.set_secure_cookie("incorrect", str(int(incorrect)+1))
            self.write('<center>Something Wrong With Your Data <a href="/">Go Home</a></center>')

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", '/'))
        # self.redirect(self.get_argument("next", self.reverse_url("main")))
