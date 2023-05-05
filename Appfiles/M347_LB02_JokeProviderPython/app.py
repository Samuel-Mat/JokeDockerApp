from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
import json

serverPort = 3000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{\"joke\":\"Programming jokes are fun ... but only when executed properly.\"}", "utf-8"))

if __name__ == "__main__":   
    webServer = HTTPServer(("", serverPort), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")