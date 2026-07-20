from dotenv import load_dotenv
load_dotenv()

import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent # myapp

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")
    JWT_SECRET_KEY = "jwt-secret-key"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Access token berlaku 15 menit
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

    # Refresh token berlaku 7 hari
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    
    
    
    """
    
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:password@localhost/mydatabase"
    )
    
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg://user:password@localhost/mydatabase"
    )
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR} / 'db.sqlite3'"
    )
    
    """