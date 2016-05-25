import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.web import RequestHandler, Application

import uimodules


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        #entries = self.db.query("SELECT * FROM entries ORDER BY date DESC"))
        entries = ["1", "2"]
        self.render("home.html", entries=entries)

class EntryHandler(tornado.web.RequestHandler):
    def get(self, entry_id):
        #entry = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        entries = ["1", "2"]
        if not entry: raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)

settings = {
        "ui_modules": uimodules,
        }

class MainHandler(RequestHandler):
    def get(self):
        if not self.get_cookie("name"):
            self.set_cookie("name", "maaoyu")
            self.write("name:maaoyu")
        else:
            self.write(self.get_cookie("name"))
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/entry/([0-9]+)", EntryHandler),
    ], **settings)

application.listen(8081)
tornado.ioloop.IOLoop.instance().start()
