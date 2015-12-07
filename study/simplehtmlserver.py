import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

application = tornado.web.Application([
	(r"/",MainHandler),
	],
	template_path=os.path.join(os.getcwd(),"templates"),
	static_path=os.path.join(os.getcwd(),"static")
)

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
