from myapp.features.surat.models.klasifikasi_surat import KlasifikasiSurat
from myapp.extensions import db
from sqlalchemy import select

from myapp.features.surat.repository.surat_repository import SuratRepository

class KlasifikasiSuratRepository:
    def __init__(self, session=None):
        if session is None:
            session = db.session
        self.session = session
        
    def get_by_surat(self) -> list[KlasifikasiSurat]:
        surat = SuratRepository().get_all()
        daftar_kode_surat = [
            value.kode_surat
            for value in surat
        ]
        
        hasil = self.filter_by_kode(daftar_kode_surat)
        return hasil
        
    def filter_by_kode(self, kode: list[str]) -> list[KlasifikasiSurat]:
        return self.session.scalars(select(KlasifikasiSurat).where(KlasifikasiSurat.kode.in_(kode))).all()
        
    def get_all(self) -> list[KlasifikasiSurat]:
        return self.session.scalars(select(KlasifikasiSurat)).all()
    
    def get_by_id(self, id) -> KlasifikasiSurat | None:
        return self.session.get(KlasifikasiSurat, id)
        
    def get_by_kode(self, kode: str) -> KlasifikasiSurat | None:
        hasil = self.session.scalars(
            select(KlasifikasiSurat)
            .where(KlasifikasiSurat.kode == kode)
        )
        
        return hasil.first()