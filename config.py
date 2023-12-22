"""Flask config"""
from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    """Base configuration class."""

    SECRET_KEY = config("SECRET_KEY")
    FLASK_APP = config("FLASK_APP")
    # static assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = config("COMPRESSOR_DEBUG")
    DEBUG = True
