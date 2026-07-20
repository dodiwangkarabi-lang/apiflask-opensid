from flask_jwt_extended import get_jwt_identity

from myapp.extensions import db
from myapp.models import User


def get_current_user():
    user_id = get_jwt_identity()

    return db.session.get(User, user_id)