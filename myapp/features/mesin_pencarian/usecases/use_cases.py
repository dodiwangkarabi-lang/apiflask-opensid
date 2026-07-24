


# ----- service -----
from myapp.features.mesin_pencarian.services import SearchEngine

# ----- repo -----
from myapp.features.surat import models
from myapp.features.surat import repository

from myapp.config import BASE_DIR

INDEX_DIR = BASE_DIR / "media" / "index"

# ----- helper -----
from .helpers import (
    MODEL_PENCARIAN_SURAT_KELUAR, MODEL_PENCARIAN_SURAT_MASUK
)

class BuildModelUC:
    def __init__(self, tipe="surat_keluar"):
        if tipe == "surat_masuk":
            self.search_engine = MODEL_PENCARIAN_SURAT_KELUAR.search_engine
            self.repo = MODEL_PENCARIAN_SURAT_KELUAR.repo
        elif tipe == "surat_keluar":
            self.search_engine = MODEL_PENCARIAN_SURAT_MASUK.search_engine
            self.repo = MODEL_PENCARIAN_SURAT_MASUK.repo
        else:
            self.search_engine = MODEL_PENCARIAN_SURAT_KELUAR.search_engine
            self.repo = MODEL_PENCARIAN_SURAT_KELUAR.repo

    def _build(self, text_field: str="isi_singkat"):
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
            for surat in self.repo.get_all()
        ]
            
        self.search_engine.build(documents, text_field)
        
        
    def execute(self, text_field: str="isi_singkat"):
        self._build(text_field)


class SearchEngineUseCase:
    def __init__(self, search_engine =None, repo=None, tipe=""):
        """
        pencarian use cases

        Args:
            search_engine (_type_, optional): _description_. Defaults to None.
            repo (_type_, optional): _description_. Defaults to None.
            tipe (str, optional): adalah tipe surat (surat masuk, surat keluar, arsip). Defaults to "".
        """
        self.search_engine = search_engine
        self.repo = repo
        
        if self.search_engine is None:
            self._set_search_engine(tipe)
        
    def _set_search_engine(self, tipe: str=""):
        if tipe == "surat_masuk":
            self.search_engine = SearchEngine(
                index_file=INDEX_DIR / "index_surat_masuk.pkl"
            )
        elif tipe == "surat_keluar":
            self.search_engine = SearchEngine(
                index_file=INDEX_DIR / "index.pkl"
            )
        elif tipe == "arsip":
            self.search_engine = SearchEngine(
                index_file=INDEX_DIR / "index_arsip.pkl"
            )
        else:
            self.search_engine = SearchEngine(
                index_file=INDEX_DIR / "index.pkl"
            )
        
    
    def build(self, documents: list[dict] = [], text_field: str="isi_singkat"):
        if self.repo is None:
            self.repo = repository.SuratKeluarRepository()
            
        if documents:
            pass
        else:
        
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
                for surat in self.repo.get_all()
            ]
            
        self.search_engine.build(documents, text_field)
    
    def search(self, keyword: str, top_k: int = 20, **kwargs) -> list[dict]:
        """

        Args:
            keyword (str): _description_
            top_k (int, optional): _description_. Defaults to 20.
            **kwargs: surat_masuk: bool = True

        Returns:
            list[dict]: _description_
        """
        # if self.kwargs.get("surat_keluar"):
        #     search_engine_service = SearchEngine(
        #         index_file = INDEX_DIR / "index.pkl"
        #     )
        #     self.search_engine = search_engine_service
        
        # if kwargs.get("surat_masuk"):
        #     search_engine_service = SearchEngine(
        #         index_file=INDEX_DIR / "index_surat_masuk.pkl"
        #     )
        #     self.search_engine = search_engine_service
        
        self.search_engine.load()
        
        return self.search_engine.search(keyword)