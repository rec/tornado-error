from __future__ import absolute_import, division, print_function, unicode_literals

import httplib
import os
import traceback

import tornado.web

GENERIC_PAGE = """<html>
  <title>%(code)d: %(message)s</title>
  <body class='bodyErrorPage'>
    %(code)d: %(message)s
  </body>
</html>"""

class ErrorHandler(tornado.web.RequestHandler):
  """A generic Tornado error response page."""
  def __init__(self, application, request, status_code):
    super(ErrorHandler, self).__init__(application, request)
    print(application, request)
    self.set_status(status_code)

  def get_error_html(self, status_code, **kwds):
    try:
      # self.require_setting('static_path')
      # TODO: why does require_setting fail when I clearly DO have a static path?
      filename = os.path.join(self.settings['static_path'], '%d.html' % status_code)
      with open(filename) as f:
        return f.read()
    except:
      print(traceback.format_exc())
      return GENERIC_PAGE % {'code': status_code,
                             'message': httplib.responses[status_code]}

  def prepare(self):
    raise tornado.web.HTTPError(self._status_code)


