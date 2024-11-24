import BaseHTTPServer
import SimpleHTTPServer

PORT = 8089

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = BaseHTTPServer.HTTPServer(('localhost', PORT), Handler)

print "Server started on port", PORT

httpd.serve_forever()
