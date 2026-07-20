from sqlalchemy import select
from myapp.extensions import db

class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def get(cls, id):
        return db.session.get(cls, id)

    @classmethod
    def all(cls):
        return db.session.scalars(select(cls)).all()