#!/usr/bin/python3
import http.server
import json
import socketserver


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # ROOT endpoint: /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # /data endpoint
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data).encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Undefined endpoints (404)
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            error_msg = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_msg).encode())


# Run server
if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server running on port {PORT}...")
        httpd.serve_forever()
