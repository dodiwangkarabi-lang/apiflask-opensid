from dataclasses import dataclass
from datetime import datetime
# from typing import List, Dict

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

@dataclass
class ModelKlasifikasi:
    id: int
    nama: str
    algoritma: str
    path: str
    created_at: datetime
    updated_at: datetime
    model: RandomForestClassifier
    is_trained: bool
    
    def latih(self, vectorizer: TfidfVectorizer, label: list[int]):
        self.model.fit(vectorizer, label)
        self.is_trained = True
        
    def prediksi(self, vectorizer: TfidfVectorizer):
        if self.is_trained:
            return self.model.predict(vectorizer)
        else:
            raise Exception("Model belum dilatih")
    
@dataclass
class Vectorizer:
    id: int
    nama: str
    algoritma: str
    path: str
    created_at: datetime
    updated_at: datetime
    vectorizer: TfidfVectorizer
    is_trained: bool
    
@dataclass
class Surat:
    id: int
    no_surat: str
    isi: str
    