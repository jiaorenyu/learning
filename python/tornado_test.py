import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        self.write("Post Hello World!")
        print(self.request.body)

    
application = tornado.web.Application([
                            (r"/", MainHandler),
                            ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
