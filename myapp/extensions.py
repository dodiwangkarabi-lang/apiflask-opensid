from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from myapp.features import klasifikasi

db = SQLAlchemy()
jwt = JWTManager()

klasifikasi = klasifikasi


# vectorizer = services.VectorizerService("")