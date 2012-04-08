"""
Serves files out of its current directory.
Doesn't handle POST requests.
"""
import SocketServer
import SimpleHTTPServer
import sys

import algo

PORT = int(sys.argv[1])

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    print self.path
    if self.path.startswith('/fakealbum'):
      self.send_response(200)
      self.send_header('Content-type','image/jpeg')
      self.end_headers()
      image_data = algo.generate(self.raw_requestline)
      self.wfile.write(image_data)
      return
    else:
      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
      return

httpd = SocketServer.ThreadingTCPServer(("0.0.0.0", PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()
