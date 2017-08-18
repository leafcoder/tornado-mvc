#-*- coding: utf-8 -*-

import os
import posixpath
import tornado.web
from my_project.config import global_config

# 首页处理类
class PortalHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

# 需要登录的处理类
class AuthHandler(tornado.web.RequestHandler):

    @tornado.web.authenticated
    def get(self):
        self.render('auth.html')
