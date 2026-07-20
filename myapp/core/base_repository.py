# from __future__ import annotations

# from typing import Generic, TypeVar

# from sqlalchemy import select

# from myapp.extensions import db

# ModelType = TypeVar("ModelType")


# class BaseRepository(Generic[ModelType]):
#     model: type[ModelType]

#     @property
#     def session(self):
#         return db.session

#     def create(self, **kwargs) -> ModelType:
#         obj = self.model(**kwargs)
#         self.session.add(obj)
#         self.session.commit()
#         self.session.refresh(obj)
#         return obj

#     def get(self, id: int) -> ModelType | None:
#         return self.session.get(self.model, id)

#     def get_all(self) -> list[ModelType]:
#         return self.session.scalars(select(self.model)).all()

#     def update(self, obj: ModelType, **kwargs) -> ModelType:
#         for key, value in kwargs.items():
#             setattr(obj, key, value)

#         self.session.commit()
#         self.session.refresh(obj)
#         return obj

#     def delete(self, obj: ModelType) -> None:
#         self.session.delete(obj)
#         self.session.commit()


from __future__ import annotations

from typing import Any, Generic, TypeVar

from sqlalchemy import select

from myapp.extensions import db

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    model: type[ModelType]

    @property
    def session(self):
        return db.session

    def create(self, **kwargs) -> ModelType:
        obj = self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get(self, id: Any) -> ModelType | None:
        return self.session.get(self.model, id)

    def get_all(self) -> list[ModelType]:
        return self.session.scalars(select(self.model)).all()

    def filter(self, *criteria) -> list[ModelType]:
        stmt = select(self.model).where(*criteria)
        return self.session.scalars(stmt).all()

    def filter_by(self, **kwargs) -> list[ModelType]:
        stmt = select(self.model).filter_by(**kwargs)
        return self.session.scalars(stmt).all()

    def first(self, *criteria) -> ModelType | None:
        stmt = select(self.model).where(*criteria)
        return self.session.scalar(stmt)

    def first_by(self, **kwargs) -> ModelType | None:
        stmt = select(self.model).filter_by(**kwargs)
        return self.session.scalar(stmt)

    def update(self, obj: ModelType, **kwargs) -> ModelType:
        for key, value in kwargs.items():
            setattr(obj, key, value)

        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, obj: ModelType) -> None:
        self.session.delete(obj)
        self.session.commit()
        
    def exists(self, *criteria) -> bool:
        return self.first(*criteria) is not None


    def exists_by(self, **kwargs) -> bool:
        return self.first_by(**kwargs) is not None


    def count(self, *criteria) -> int:
        stmt = select(self.model)

        if criteria:
            stmt = stmt.where(*criteria)

        return len(self.session.scalars(stmt).all())
    
"""
Usage:

from myapp.core import BaseRepository
from myapp.features.surat import models


class SuratMasukRepository(BaseRepository[models.SuratMasuk]):
    model = models.SuratMasuk
    

class SuratKeluarRepository(BaseRepository[models.SuratKeluar]):
    model = models.SuratKeluar
"""