from ..domain import entity

class PreprocessingService:
    def __init__(self, surat_repository, vectorizer: entity.Vectorizer) -> None:
        self.surat_repository = surat_repository
        self.vectorizer = vectorizer    
    
    def transform(self, surat: entity.Surat):
        hasil = self.vectorizer.vectorizer.transform([surat.isi])
        return hasil
    
    def transform_banyak(self, surat_list: list[entity.Surat]):
        hasil = self.vectorizer.vectorizer.transform([surat.isi for surat in surat_list])
        return hasil