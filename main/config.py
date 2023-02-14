import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TESTING = False
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    DATABASE_BASE_URL = os.getenv("DATABASE_BASE_URL")
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_BASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}"
