#-*- coding: utf-8 -*-

from my_project.urls import urls
from my_project.config import global_config
from my_project.controller import ErrorController

import tornado.web
import tornado.locale
from tornado.httpclient import AsyncHTTPClient

# 切换 AsyncHTTPClient 底层获取 HTTP 报文库为 curl
AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')

# 加载本地化目录中的本地化翻译文件
tornado.locale.load_translations(global_config.locale_dir)

def make_app(**setting):
    '''生成并返回一个 Application 对象'''
    args = {}
    args.update(global_config.default_setting)
    args['default_handler_class'] = ErrorController.E404Handler
    args.update(setting)
    return tornado.web.Application(urls, **args)
