#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys; sys.dont_write_bytecode = True

from my_project.application import make_app
from my_project.config import global_config

import tornado.ioloop

if __name__ == "__main__":
    app = make_app()
    app.listen(global_config.port, address=global_config.address)
    tornado.ioloop.IOLoop.current().start()
