import tornado.ioloop
import tornado.web
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the index context route")


class HelloWorld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!!!!")


def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/api", HelloWorld),
    ])
 

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

