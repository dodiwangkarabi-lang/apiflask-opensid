# from __future__ import annotations
from typing import Any, Generic, TypeVar, TYPE_CHECKING, List
from sqlalchemy import select, union_all
from myapp.extensions import db
from myapp.features.surat import models

# if TYPE_CHECKING:
    # from ..models import SuratMasuk,  SuratKeluar

from ..models import SuratMasuk,  SuratKeluar

# ----- dto -----
# from myapp.features.shared.dto import dto


# from myapp.utils import paginasi
from myapp.features.core.utils import paginated

class SuratMasukRepository:
    def __init__(self, session=None):
            if session is None:
                session = db.session
            self.session = session
            
    
    def tambah(self, **kwargs) -> SuratMasuk:
        obj = SuratMasuk(**kwargs)
        self.session.add(obj)
        self.session.flush()
        # self.session.commit()
        self.session.refresh(obj)
        
        return obj
    
    
    def edit(self, id: int, **kwargs) -> SuratMasuk | None:
        obj = self.session.get(SuratMasuk, id)
        if obj is None:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
            
        self.session.flush()
        self.session.refresh(obj)
        
        # ----- KALAU TIDAK MAU DI LEMPAR KE SERVICE MENUTUP SESSION -----
        # self.session.commit()
        # self.session.refresh(obj)
        
        return obj
    
    def hapus(self, id: int) -> None:
        obj = self.session.get(SuratMasuk, id)
        if obj is None:
            return None
        self.session.delete(obj)
        # self.session.commit()
        return obj
        
    def lihat(self, id: int) -> SuratMasuk | None:
        hasil = self.session.get(SuratMasuk, id)
        return hasil
    
    def lihat_semua(self) -> list[SuratMasuk]:
        return self.session.scalars(select(SuratMasuk)).all()
    
class SuratKeluarRepository:
    def __init__(self, session=None):
        if session is None:
            session = db.session
        self.session = session
        
    def tambah(self, **kwargs) -> SuratKeluar:
        obj = SuratKeluar(**kwargs)
        self.session.add(obj)
        # self.session.commit()
        self.session.refresh(obj)
        return obj
    
    def edit(self, id: int, **kwargs) -> SuratKeluar:
        obj = self.session.get(SuratKeluar, id)
        if obj is None:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        # self.session.commit()
        self.session.flush()
        self.session.refresh(obj)
        return obj
    
    def hapus(self, id: int) -> None:
        obj = self.session.get(SuratKeluar, id)
        if obj is None:
            return None
        self.session.delete(obj)
        # self.session.commit()
        return obj
        
    def lihat(self, id: int) -> SuratKeluar | None:
        return self.session.get(SuratKeluar, id)
    
    def lihat_semua(self) -> list[SuratKeluar]:
        return self.session.scalars(select(SuratKeluar)).all()

class SuratRepository:
    def __init__(self, session=None):
        if session is None:
            session = db.session
        self.session = session
    
    # @property
    # def session(self):
    #     return db.session
    
    def get_by_tipe_surat(self, tipe_surat: str) -> list[SuratKeluar | SuratMasuk] | None:
        if tipe_surat == "surat_masuk":
            return self.session.scalars(
                select(SuratMasuk)
                # .where(SuratMasuk.berkas_scan.is_not(None))
            ).all()
        elif tipe_surat == "surat_keluar":
            return self.session.scalars(
                select(SuratKeluar)
                # .where(SuratKeluar.berkas_scan.is_not(None))
            ).all()
            
        return None
        
    
    
    def get_all(self) -> list[SuratKeluar | SuratMasuk]:
        surat_keluar = self.session.scalars(
            select(SuratKeluar)
            .where(SuratKeluar.berkas_scan.is_not(None))
        ).all()

        surat_masuk = self.session.scalars(
            select(SuratMasuk)
            .where(SuratMasuk.berkas_scan.is_not(None))
        ).all()

        return surat_keluar + surat_masuk
    
    def get_by_kode_surat(self, kode: str) -> list[SuratKeluar | SuratMasuk] | None:
        surat_keluar = self.session.scalars(
            select(SuratKeluar)
            .where(SuratKeluar.kode_surat == kode)
        ).all()

        surat_masuk = self.session.scalars(
            select(SuratMasuk)
            .where(SuratMasuk.kode_surat == kode)
        ).all()

        return surat_keluar + surat_masuk
    
    def semua_surat(self, page=None, page_size=10, **kwargs):
        if page is None:
            page = 1
        surat_masuk_atau_keluar = self.get_all()
        hasil = [
            {
                "id": value.id,
                "tipe_surat": "surat_masuk" if isinstance(value, SuratMasuk) else "surat_keluar",
                "surat": value
            }
            for value in surat_masuk_atau_keluar
        ]
        
        hasil = paginated(hasil, page=page, page_size=page_size)

        return hasil
    
    def get_by_isi_singkat(self, isi_singkat: str) -> list[SuratKeluar | SuratMasuk] | None:
        surat_keluar = self.session.scalars(
            select(SuratKeluar)
            .where(SuratKeluar.isi_singkat.contains(isi_singkat))
        ).all()

        surat_masuk = self.session.scalars(
            select(SuratMasuk)
            .where(SuratMasuk.isi_singkat.contains(isi_singkat))
        ).all()
        
        return surat_keluar + surat_masuk
    
    
    def get_by_id(self, id: int, jenis="surat_masuk") -> SuratMasuk | SuratKeluar:
        if jenis == "surat_masuk":
            return self.session.get(SuratMasuk, id)
        elif jenis == "surat_keluar":
            return self.session.get(SuratKeluar, id)