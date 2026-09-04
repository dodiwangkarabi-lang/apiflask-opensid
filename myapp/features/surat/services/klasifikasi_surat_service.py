from myapp.extensions import klasifikasi
# from myapp.extensions import model_klasifikasi, vectorizer
entity = klasifikasi.entity

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import SuratMasuk, SuratKeluar

from typing import Any

class KlasifikasiSuratService:
    def __init__(self, surat: "SuratMasuk | SuratKeluar"):
        self.surat = surat
    
    @property
    def vectorizer(self) -> entity.Vectorizer:
        service = klasifikasi.services.VectorizerService("contoh")
        vectorizer = service.load_vectorizer("contoh.joblib")
        
        return vectorizer
    
    @property
    def classifier(self) -> entity.ModelKlasifikasi:
        service = klasifikasi.services.ModelService("contoh")
        model_klasifikasi = service.load_model("contoh.joblib")
        
        return model_klasifikasi
        
    def prediksi(self) -> str:
        x_test = self.vectorizer.transform(self.surat.kode_surat)
        hasil = self.classifier.prediksi(x_test)
        return hasil[0]