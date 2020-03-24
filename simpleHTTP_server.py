import SimpleHTTPServer
import SocketServer

## put this in a special folder you create and include
## index.html and just text files

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer( ("localhost", PORT) , Handler  )

httpd.serve_forever()
