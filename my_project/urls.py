#-*- coding: utf-8 -*-

import posixpath
import tornado.web

from my_project.config import global_config
from my_project.controller import PortalController, ErrorController

# 静态文件对应各自的网络访问路径
statics_urls = []
statics_urls.append(
    (r'/static/(.*)', tornado.web.StaticFileHandler, {
        'path': posixpath.join(global_config.view_base, 'static')
    })
)

urls = [
    (r'/(?:index.html)?', PortalController.PortalHandler),      # 首页
    (r'/auth', PortalController.AuthHandler),                   # 需要登录
    (r'/404', ErrorController.E404Handler),                     # 错误页
]
urls.extend(statics_urls)

# 限制 Host 匹配才能访问
from tornado.routing import HostMatches
urls = [
    (HostMatches('0.0.0.0'), urls),
    (HostMatches('127.0.0.1'), urls),
    (HostMatches('localhost'), urls)
]
