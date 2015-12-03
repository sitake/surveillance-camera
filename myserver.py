import tornado.ioloop
from tornado.ioloop import PeriodicCallback
import tornado.web
import tornado.websocket
import os
import cv2

FRAME_SPEED = 200

class SendWebSocket(tornado.websocket.WebSocketHandler):
	
	userlist = []


	@classmethod
	def updateImage(cls):
		ret,image = cls.cap.read()
		if ret:
			image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
			cv2.imwrite("dist/image0.png",image)
			map(lambda soc:soc._send_message(),cls.userlist)

	@classmethod
	def socinit(cls):
		cls.cap = cv2.VideoCapture(0)
		cls.callback = PeriodicCallback(cls.updateImage,FRAME_SPEED)
		cls.callback.start()
	
	@classmethod
	def socdest(cls):
		cls.cap.release()
		cls.callback.stop()
	def check_origin(self,origin):
		print(origin)
		return True

	def open(self):
		if len(self.__class__.userlist) == 0:
			print("checkcheckcheck")
			self.__class__.socinit()

		self.__class__.userlist.append(self)
		print(self.__class__.userlist)
		print('WebSocket opened')

	def on_message(self, message):
		print(message)

	def _send_message(self):
		self.write_message("0")

	def on_close(self):
		self.__class__.userlist.remove(self)
		if len(self.__class__.userlist) == 0:
			print("kibisikune")
			self.__class__.socdest()
		print('WebSocket closed')
		print(self.__class__.userlist)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")
application = tornado.web.Application([
	(r"/",MainHandler),
	(r'/test',SendWebSocket),
	],
	template_path=os.path.join(os.getcwd(),"templates"),
	static_path=os.path.join(os.getcwd(),"dist")
)

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
