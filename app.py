from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class StaticPageHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    server = ThreadingHTTPServer((host, port), StaticPageHandler)
    print(f"Serving http://{host}:{port}")
    print("Press Ctrl+C to stop the server")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server.server_close()