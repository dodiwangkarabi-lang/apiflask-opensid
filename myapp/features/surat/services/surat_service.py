from ..models import SuratKeluar, SuratMasuk
from ..repository import SuratRepository


class SuratService:
    def __init__(self, surat_repository: SuratRepository):
        self.surat_repository = surat_repository
        
    def get_all(self) -> list[SuratKeluar | SuratMasuk]:
        return self.surat_repository.get_all()
    
    def get_by_id(self, id: int, jenis="surat_masuk") -> SuratMasuk | SuratKeluar:
        return self.surat_repository.get_by_id(id, jenis)