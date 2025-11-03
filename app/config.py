"""Application configuration using environment variables."""

import os

# Use environment variables for sensitive data
API_KEY = os.getenv("API_KEY", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "myapp",
    "user": "admin",
    "password": DB_PASSWORD,
}

# More configuration
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}
