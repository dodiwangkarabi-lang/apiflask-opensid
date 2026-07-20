# auth/repository.py

from myapp.core import BaseRepository

from myapp.extensions import db
from myapp.features.auth.models import User

# ----- sqlalchemy -----
from sqlalchemy import select

class UserRepository(BaseRepository[User]):
    model = User

def get_user_by_id(user_id: int) -> User | None:
    return db.session.get(User, user_id)


def get_user_by_username(username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    return db.session.scalar(stmt)


def get_user_by_email(email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    return db.session.scalar(stmt)

def list_users() -> list[User]:
    stmt = select(User).order_by(User.username)
    return list(db.session.scalars(stmt))


def create_user(**data) -> User:
    user = User(**data)

    db.session.add(user)
    db.session.commit()

    return user


def update_user(user: User) -> User:
    db.session.commit()
    return user


def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()