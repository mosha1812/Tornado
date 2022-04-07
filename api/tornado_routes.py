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


class HomeHandler(tornado.web.RequestHandler):
    """
    """
    def get(self):
        """
        GET /home
        """
        self.render("../html/home.html")


class WeatherHandler(tornado.web.RequestHandler):
    """    
    """
    def get(self):
        """
        GET /weather?degree=35
        """
        degree = int(self.get_argument("degree"))
        output = "Hot" if degree > 20 else "Cold"
        drink = "Beer" if degree > 20 else "Hot Beverage"
        self.render("../html/weather.html", output = output, drink = drink)


