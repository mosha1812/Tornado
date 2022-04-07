import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """
    Simple Handler for Health Check.
    """
    def get(self):
        """
        GET /
        """
        self.write(f"<h1>Found Server Running!!!</h1>")


class HelloWorldApiHandler(tornado.web.RequestHandler):
    """
    Simple Class to handle Hello World API call.
    """
    def get(self):
        """
        GET /helloWorld
        """
        self.write("Hello World!!!!")