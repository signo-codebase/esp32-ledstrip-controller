from http.server import BaseHTTPRequestHandler, HTTPServer
import re
from urllib.parse import urlparse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/color':
            # Extract RGB values using regular expressions
            query_string = parsed_path.query
            red_match = re.search(r'r=(\d+)', query_string)
            green_match = re.search(r'g=(\d+)', query_string)
            blue_match = re.search(r'b=(\d+)', query_string)

            red = red_match.group(1) if red_match else ''
            green = green_match.group(1) if green_match else ''
            blue = blue_match.group(1) if blue_match else ''

            # Print or use the extracted RGB values
            print(f'Red: {red}')
            print(f'Green: {green}')
            print(f'Blue: {blue}')

            # Send a response (optional)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Red: {red}\nGreen: {green}\nBlue: {blue}'.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server...')
    httpd.serve_forever()
