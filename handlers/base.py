import tornado.web
import sys
import torndb
import subprocess
import datetime, time
import os, re, struct
import signal
import socket, hashlib
from tornado import iostream
from tornado import ioloop
from lib2to3.fixer_util import String
from macpath import split
from __builtin__ import int

# sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import settings
<<<<<<< HEAD
#from models.models import DB_Session
=======
from models.models import DB_Session
>>>>>>> 87319db5d0b5ee11cb1dcfe00c116d092b99fb95

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.classname = self.__class__.__name__
        self.user_header = self.get_secure_cookie
<<<<<<< HEAD
        #self.session = DB_Session()
=======
        self.session = DB_Session()
>>>>>>> 87319db5d0b5ee11cb1dcfe00c116d092b99fb95

    def get_current_user(self):
        return self.get_secure_cookie('user')

    @property
    def db(self):
        db = torndb.Connection(settings.DBINFO['dbhost'], settings.DBINFO['dbname'],
                               settings.DBINFO['dbuser'], settings.DBINFO['dbpasswd'])

        return db


    def timeout_command(self, cmd, timeout):
        time_start = datetime.datetime.now()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while process.poll() is None:
            time.sleep(0.2)
            time_now = datetime.datetime.now()
            if (time_now - time_start).seconds > timeout:
                os.kill(process.pid, signal.SIGILL)
                os.waitpid(process.pid)
                return "False error timeout"
        return process.stdout.read()
        
<<<<<<< HEAD
    # def on_finish(self):
    #     #self.session.close()
    #     pass
=======
    def on_finish(self):
        self.session.close()
>>>>>>> 87319db5d0b5ee11cb1dcfe00c116d092b99fb95
