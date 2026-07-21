


# ----- service -----
from myapp.features.mesin_pencarian.services import SearchEngine

# ----- repo -----
from myapp.features.surat import models
from myapp.features.surat import repository

from myapp.config import BASE_DIR

INDEX_DIR = BASE_DIR / "media" / "index"

search_engine = SearchEngine(
    index_file = INDEX_DIR / "index.pkl"
)


class SearchEngineUseCase:
    def __init__(self, search_engine=search_engine, repo=None):
        self.search_engine = search_engine
        self.repo = repo
        
    def build(self, documents: list[dict], text_field: str="isi_singkat"):
        surat_keluar_repo = repository.SuratKeluarRepository()
        documents = [
            {
                "id": surat.id,
                "isi_singkat": surat.isi_singkat,
                "nomor_surat": surat.nomor_surat,
                "tanggal_surat": surat.tanggal_surat,
                "lokasi_arsip": surat.lokasi_arsip,
                "nomor_urut": surat.nomor_urut,
                "kode_surat": surat.kode_surat
            }
            for surat in surat_keluar_repo.get_all()
        ]
        self.search_engine.build(documents, text_field)
    
    def search(self, keyword: str, top_k: int = 20) -> list[dict]:
        self.search_engine.load()
        
        return self.search_engine.search(keyword)