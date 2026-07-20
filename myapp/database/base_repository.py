# base_repository.py

from typing import Generic, TypeVar
from sqlalchemy import select
from myapp.extensions import db

T = TypeVar("T")


class BaseRepository(Generic[T]):

    model: type[T]

    @classmethod
    def get(cls, id: int):
        return db.session.get(cls.model, id)

    @classmethod
    def list(cls):
        return db.session.scalars(select(cls.model)).all()

    @classmethod
    def create(cls, **kwargs):
        obj = cls.model(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj