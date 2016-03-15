#!/usr/bin/python
# -*- coding=utf-8 -*-

import logging
import logging.handlers
import time
import redis
import paramiko
import os
import random
import uuid
import base64

#get logger
#func
def get_log(logname='test.log', loglevel=1, logger=''):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(logger)
    loglevels = {0:logging.NOTSET, 1:logging.DEBUG, 2:logging.INFO, 3:logging.WARNING, 4:logging.ERROR, 5:logging.CRITICAL}
    loglevel = loglevels[int(loglevel)]
    logger.setLevel(loglevel)
    format = "%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s"
    formater = logging.Formatter(format)
    handler = logging.handlers.TimedRotatingFileHandler("%s.log" % logname , "M", 1, 0)
    handler.suffix = "%Y%m%d.%H%M"
    handler.setFormatter(formater)
    logger.addHandler(handler)
    return logger

#class 
class Logger():
    def __init__(self, logname='test.log', loglevel=1, logger=''):
      loglevels = {0:logging.NOTSET, 1:logging.DEBUG, 2:logging.INFO, 3:logging.WARNING, 4:logging.ERROR, 5:logging.CRITICAL}
      self.loglevel = loglevels[int(loglevel)]
      
      # 创建一个logger
      self.logger = logging.getLogger(logger)
      self.logger.setLevel(self.loglevel)
      
      # 创建一个handler，用于写入日志文件
      fh = logging.FileHandler(logname)
      fh.setLevel(self.loglevel)

        # 再创建一个handler，用于输出到控制台
      ch = logging.StreamHandler()
      ch.setLevel(self.loglevel)
      
      # 定义handler的输出格式
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      fh.setFormatter(formatter)
      ch.setFormatter(formatter)

      # 给logger添加handler
      self.logger.addHandler(fh)
      self.logger.addHandler(ch)
      
      def getlog(self):
        return self.logger
  #test
  #logger = Logger(logname='log.txt', loglevel=1, logger="fuck").getlog()
  
  #get redis_client
  class BaseRedis():
    def __init__(self, kwarg):
        self.host = kwarg.get('host')
        self.port = kwarg.get('port', 6379)
        self.db = kwarg.get('db', 0)
        self.password = kwarg.get('password', '')
        self.timeout = kwarg.get('timeout', 3)
        self.pool = redis.ConnectionPool(host=self.host, password=self.password, port=self.port, db=self.db, socket_timeout=self.timeout)

    def connect(self):
        r = redis.Redis(connection_pool=self.pool)
        return r
        
  #get ssh on paramiko
  class PYSSH(object):
    def __init__(self,dic):
        self.host = dic.get('host')
        self.port = dic.get('port',22)
        self.user = dic.get('user')
        self.password = dic.get('password', '')
        self.timeout = dic.get('timeout', 5)
        self.outlog = dic.get('outlog', 'outlog.log')
        self.ssh = paramiko.SSHClient()
        paramiko.util.log_to_file(self.outlog)
        self.flag = False
        self.failed_host = []
    def connect(self):
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.password:
                self.ssh = self.ssh.connect(host=self.host, port=self.port, user=self.user, password=self.password,timeout=self.timeout)
            else:
                pkey_file =os.path.expanduser( '.ssh/id_rsa')
                key_file_pwd = '123456'  #私钥密码
                try:
                    key = paramiko.RSAKey.from_private_key_file(pkey_file)
                    #key = paramiko.DSSKey.from_private_key_file(pkey_file)
                except paramiko.PasswordRequiredException:
                    key = paramiko.RSAKey.from_private_key_file(pkey_file,key_file_pwd)
                self.ssh = self.ssh.connect(host=self.host, port=self.port, user=self.user, pkey=key, timeout=self.timeout)
            self.flag = True
        except Exception,e:
            self.failed_host.append(self.host)
            pass
    def run(self,cmd):
        results = {}
        exit_code = 0
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if len(stderr.readlines()) > 0:
            exit_code = -1
            results['exit_code'] = exit_code
            results['result'] = stderr.readlines()
        else:
            results['exit_code'] = exit_code
            results['result'] = stdout.readlines()
        return results

    def get_sftp_client(self):
        if not self.flag:
            self.ssh.connect()
        sftp_client = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        #sftp_client = self.ssh.open_sftp()
        return sftp_client
  
  #sudo root用户操作      
  def sudoroot_ssh(host,username,password,port,root_pwd,cmd):
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = host,port=int(port),username=username, password=password)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        buff = ''
        while not buff.endswith('Password: '):
            resp = ssh.recv(9999)
            buff +=resp
        ssh.send(root_pwd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff +=resp
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff +=resp
        s.close()
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        s.close()
    return result

#get unique id
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
ccount = len(chars)-1
def get_unique_id():
    s = ''
    for i in xrange(0,9):
        s += chars[random.randint(0,ccount)]
    return s

#get secret cookie
def create_cookie_secret():
    return base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    
    
    
