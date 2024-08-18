import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from routes import handle_route

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/static/"):
            self.serve_static_file(self.path[1:])
        else:
            response, content_type = handle_route(self.path, "GET")
            self.respond(response, content_type)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        form_data = parse_qs(post_data.decode('utf-8'))
        response, content_type = handle_route(self.path, "POST", form_data)
        self.respond(response, content_type)

    def serve_static_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-Type', self.get_content_type(file_path))
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

    def respond(self, response, content_type):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def get_content_type(self, file_path):
        if file_path.endswith(".css"):
            return "text/css"
        elif file_path.endswith(".js"):
            return "application/javascript"
        elif file_path.endswith(".html"):
            return "text/html"
        else:
            return "application/octet-stream"

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
