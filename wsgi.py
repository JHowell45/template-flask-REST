"""Use this file for creating an instance of the Flask application.

This file is used for creating an instance of the Flask application for use with
Gunicorn and running the application in production.
"""
from app import create_app

app = create_app()
