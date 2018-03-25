#/usr/bin/python
# -*- coding: UTF-8 -*-

import SimpleHTTPServer
import SocketServer

# port number must be more than 7000
PORT = 8002

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
