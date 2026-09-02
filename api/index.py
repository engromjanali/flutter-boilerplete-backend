"""Vercel serverless entrypoint.

The Django project lives one directory down, so that directory is put on
sys.path before the WSGI application is built. Vercel invokes the module-level
`app` object for every request.
"""
import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent / 'flutter_boilerplete'
sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flutter_boilerplete.settings')

from django.core.wsgi import get_wsgi_application  # noqa: E402

app = get_wsgi_application()
