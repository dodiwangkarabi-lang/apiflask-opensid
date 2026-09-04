# from __future__ import annotations
import typing
from myapp.features.surat.repository.surat_repository import SuratRepository
from dataclasses import dataclass
from myapp.config import MEDIA_ROOT

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from pathlib import Path

# if typing.TYPE_CHECKING:
    # from myapp.features.surat.models import SuratMasuk, SuratKeluar

from myapp.features.surat.models import SuratMasuk, SuratKeluar

from myapp.features.surat.schema import HasilPencarianResponseSchema as HasilPencarian, SuratSchema

# @dataclass
# class HasilPencarian:
#     id: int
#     kemiripan: float
#     surat: SuratKeluar | SuratMasuk
    
#     def to_dict(self):
#         return self.__dict__
    
class AlgoritmaCosineSimilarity:
    def hitung(self, A, B):
        return cosine_similarity(A, B)

class TfIdfVectorizerRepository:
    def __init__(self, media_root: Path = MEDIA_ROOT) -> None:
        self.media_root = media_root
    
    def get_by_name(self, nama_vectorizer: str) -> TfidfVectorizer:
        return joblib.load(self.media_root / nama_vectorizer)
    
    def save(self, model, nama_vectorizer: str = "tf_idf_vectorizer.joblib"):
        joblib.dump(model, self.media_root / nama_vectorizer)
    
    def create(self, texts: typing.List[str], is_save: bool = True) -> TfidfVectorizer:
        model = TfidfVectorizer()
        model.fit(texts)
        
        if is_save:
            self.save(model, "tf_idf_vectorizer.joblib")
        return model

class PencarianSuratService:
    def __init__(
        self,
        surat_repository: SuratRepository,
        vectorizer_repository=TfIdfVectorizerRepository(),
        algoritma=AlgoritmaCosineSimilarity(),
    ):
        self.surat_repository = surat_repository
        self.vectorizer_repository = vectorizer_repository
        self.algoritma = algoritma

    def cari(self, keyword: str, kode_surat: str, nilai_kemiripan_min: float = 0.5) -> typing.List[HasilPencarian]:

        filter_surat = self.surat_repository.get_by_kode_surat(kode_surat)
        if not filter_surat:
            return []
        
        isi_surat =[]
        for surat in filter_surat:
            if surat.isi_singkat:
                isi_surat.append(surat.isi_singkat)
            else:
                isi_surat.append("")
        # isi_surat = [
        #     surat.isi_singkat
        #     for surat in filter_surat
        # ]
        vectorizer = self.vectorizer_repository.get_by_name("tf_idf_vectorizer.joblib")
        vektorisasi_keyword = vectorizer.transform([keyword])
        vektorisai_surat = vectorizer.transform(isi_surat)

        kemiripan = self.algoritma.hitung(vektorisasi_keyword, vektorisai_surat)
        # print(len(kemiripan[0]))
        # print(len(filter_surat))

        hasil = []
        for surat, nilai_kemiripan in zip(filter_surat, kemiripan[0]):
            if nilai_kemiripan < nilai_kemiripan_min:
                continue
            surat_dict = {
                "id": surat.id,
                "isi_singkat": surat.isi_singkat,
                
                "kode_surat": surat.kode_surat,
                "tanggal_surat": surat.tanggal_surat,
                "berkas_scan": surat.berkas_scan,
                "nomor_surat": surat.nomor_surat
            }
            
            hasil_pencarian = {
                "id": surat.id,
                "kemiripan": nilai_kemiripan.item(),
                "tipe_surat": "surat_masuk" if isinstance(surat, SuratMasuk) else "surat_keluar",
                "surat": surat_dict
            }
            
            # temp = HasilPencarian.load(hasil_pencarian)
            temp = hasil_pencarian
            hasil.append(
                temp
            )
            
            # print(temp)

        return hasil