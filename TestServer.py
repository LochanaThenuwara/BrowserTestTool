import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import json

PORT = 8080

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        length = int(self.headers.getheader('content-length'))        
        data_string = self.rfile.read(length)

        result = data_string
        print result

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()
