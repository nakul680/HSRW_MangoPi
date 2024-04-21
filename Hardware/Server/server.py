from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        sensor_data = json.loads(post_data.decode('utf-8'))

        # Process sensor data
        print("Received sensor data:", sensor_data)

        self._set_headers()
        response = json.dumps({'message': 'Data received successfully'})
        self.wfile.write(response.encode('utf-8'))

    def do_GET(self):
        self._set_headers()
        response = json.dumps({'message': 'GET request received successfully'})
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()