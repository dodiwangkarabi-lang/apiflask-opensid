# auth/services.py

from .repository import get_user_by_username
from werkzeug.security import check_password_hash
from .models import User


def authenticate(username: str, password: str) -> User | None:
    user = get_user_by_username(username)

    if user is None:
        return None

    if not check_password_hash(user.password_hash, password):
        return None

    return user

def login(user: User) -> dict:
    ...


def logout(user: User) -> None:
    ...


def change_password(user: User, old_password: str, new_password: str) -> bool:
    ...