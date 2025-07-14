import threading
import time
from src.server import app


class TestServer:
    """Test server wrapper for running Flask app during tests."""

    def __init__(self):
        self.app = app
        self.server_thread = None
        self.port = None
        self.base_url = None

    def start(self, port=0):
        """Start the test server on the specified port."""
        # Use a free port if 0 is specified
        if port == 0:
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', 0))
                port = s.getsockname()[1]

        self.port = port
        self.base_url = f"http://localhost:{port}"

        # Start server in a separate thread
        self.server_thread = threading.Thread(
            target=self._run_server,
            args=(port,),
            daemon=True
        )
        self.server_thread.start()

        # Wait for server to start
        time.sleep(0.5)

        return self

    def _run_server(self, port):
        """Run the Flask server."""
        self.app.run(host='localhost', port=port, debug=False, use_reloader=False)

    def stop(self):
        """Stop the test server."""
        # Flask server running in thread will stop when main thread exits
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
