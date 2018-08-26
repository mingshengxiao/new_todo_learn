#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		filename = self.get_argument('filename')
		# http头 浏览器自动识别为文件下载
		self.set_header('Content-Type', 'application/octet-stream')

		# 下载时显示的文件名称
		self.set_header('Content-Disposition', 'attachment;filename=%s' % filename)

		with open(filename, 'rb') as f:
			while True:
				data = f.read(1024)
				if not data:
					break
				self.write(data)
				self.finish()

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
		])

if __name__ == '__main__':
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()