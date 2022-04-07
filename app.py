import tornado.ioloop
import tornado.web
import json
from api.tornado_routes import MainHandler, HelloWorldApiHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/helloWorld", HelloWorldApiHandler),
    ])
 

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

