import os
import sys

# Extend root 'app' package path to include 'backend/app'
backend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend")
backend_app_dir = os.path.join(backend_dir, "app")

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

if os.path.exists(backend_app_dir) and backend_app_dir not in __path__:
    __path__.append(backend_app_dir)
