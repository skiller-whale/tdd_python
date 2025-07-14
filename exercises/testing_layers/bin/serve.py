import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))

from src.server import app

if __name__ == "__main__":
    port = 3001
    print(f"Frontend server started on http://localhost:{port}")
    app.run(debug=True, port=port, host='0.0.0.0')
