# from core.base_repository import Base

from typing import Any, Generic, TypeVar
from sqlalchemy import select, union_all
from myapp.extensions import db
from myapp.features.surat import models

class ArsipRepository():
    def __init__(self):
        pass
    
    @property
    def session(self):
        return db.session
    
    def get_all(self) -> list[models.SuratKeluar | models.SuratMasuk]:
        surat_keluar = self.session.scalars(
            select(models.SuratKeluar)
            .where(models.SuratKeluar.berkas_scan.is_not(None))
        ).all()

        surat_masuk = self.session.scalars(
            select(models.SuratMasuk)
            .where(models.SuratMasuk.berkas_scan.is_not(None))
        ).all()

        return surat_keluar + surat_masuk
    
    # def get_all(self) -> list[int]:
    #     Tabel1 = models.SuratKeluar
    #     Tabel2 = models.SuratMasuk
        
    #     stmt = union_all(
    #         select(Tabel1.id, Tabel1.berkas_scan).where(Tabel1.berkas_scan.is_not(None)),
    #         select(Tabel2.id, Tabel2.berkas_scan).where(Tabel2.berkas_scan.is_not(None)),
    #     )
        
    #     return self.session.scalars(stmt).all()