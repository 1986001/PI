import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
try:
            file_path = os.path.join(os.getcwd(), self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            with open(file_path) as f:
                self.send_header('Content-Length', len(f.read()))
            self.end_headers()
            with open(file_path, 'r') as f:
                self.copyfile(f, self.wfile)
        except FileNotFoundError:
            self.send_response(404)

def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 80...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
