import tornado.web

class E404Handler(tornado.web.RequestHandler):

    def get(self):
        self.render('_errors/404.html')
