import argparse
from http.server import SimpleHTTPRequestHandler, HTTPServer
from http import HTTPStatus

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.NO_CONTENT)
        self.end_headers()

def run(server_class=HTTPServer, port=8000, allow_all_cors=False):
    server_address = ('', port)
    handler_class = CORSRequestHandler if allow_all_cors else SimpleHTTPRequestHandler
    print(handler_class)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description='Start a simple HTTP server with CORS enabled.')
    parser.add_argument('--port', type=int, nargs='?', default=8000, help='Specify the port number (default: 8000)')
    parser.add_argument('--allow_cors', action='store_true', help='Allow All CORS')
    args = parser.parse_args()

    run(port=args.port, allow_all_cors=args.allow_cors)

if __name__ == '__main__':
    main()