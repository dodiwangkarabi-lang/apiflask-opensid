from ..domain import entity

class ModelService:
    def __init__(self, model_repository):
        self.model_repository = model_repository
    
    def load_model(self, nama_model) -> entity.ModelKlasifikasi:
        result = self.model_repository.load(nama_model)
        return result
    
    def save_model(self, data: entity.ModelKlasifikasi, nama_model: str = "") -> None:
        if not nama_model:
            nama_model = data.nama
        self.model_repository.save(data, nama_model)
        
class VectorizerService:
    def __init__(self, vectorizer_repository):
        self.vectorizer_repository = vectorizer_repository
        
    def load_vectorizer(self, nama_vectorizer) -> entity.Vectorizer:
        result = self.vectorizer_repository.load(nama_vectorizer)
        return result
    
    def save_vectorizer(self, data: entity.Vectorizer, nama_vectorizer: str = "") -> None:
        self.vectorizer_repository.save(data, nama_vectorizer)
    