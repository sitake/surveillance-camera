import tornado.ioloop
from tornado.ioloop import PeriodicCallback
import tornado.web
import tornado.websocket
import os

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class MainSocket(tornado.websocket.WebSocketHandler):
	def open(self):
		self.count = 0
		self.callback = PeriodicCallback(self.inccounter,1000)
		self.callback.start()
		print("websocket is opened")

	def inccounter(self):
		self.count += 1
		self.write_message(str(self.count))

	def on_message(self,message):
		print(message)

	def on_close(self):
		self.callback.stop()
		print("websocket is closed")

application = tornado.web.Application([
	(r"/",MainHandler),
	(r"/socket",MainSocket),
	],
	template_path=os.path.join(os.getcwd(),"templates"),
	static_path=os.path.join(os.getcwd(),"static")
)

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
