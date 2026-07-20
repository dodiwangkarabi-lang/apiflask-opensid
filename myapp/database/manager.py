from sqlalchemy import select
from myapp.extensions import db


class Manager:

    def __init__(self, model):
        self.model = model

    def all(self):
        return db.session.scalars(
            select(self.model)
        ).all()

    def get(self, id):
        return db.session.get(self.model, id)

    def filter(self, *criteria):
        return db.session.scalars(
            select(self.model).where(*criteria)
        )