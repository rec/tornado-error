import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import ErrorHandler

from tornado.options import define, options

define('port', default=8888, help='run on the given port', type=int)

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello, keywords!')

def main():
  tornado.options.parse_command_line()
  static_path = os.path.join(os.path.dirname(__file__), 'static')
  handlers = [(r'/', MainHandler)]
  application = tornado.web.Application(handlers, static_path=static_path)
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(options.port)
  tornado.web.ErrorHandler = ErrorHandler.ErrorHandler
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
