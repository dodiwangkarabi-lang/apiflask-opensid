from ..domain import entity, vo

from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import random
from datetime import datetime

class ModelKlasifikasiFactory:
    
    @staticmethod
    def create(texts: List[str], labels: List[str]) -> entity.ModelKlasifikasi:
        # Dataset
        # texts = [
        #     "Timnas Indonesia menang",
        #     "Liga Champions dimulai",
        #     "Harga BBM naik",
        #     "Bursa saham menguat",
        #     "Presiden bertemu menteri",
        #     "DPR mengesahkan undang-undang"
        # ]

        # labels = [
        #     "Olahraga",
        #     "Olahraga",
        #     "Ekonomi",
        #     "Ekonomi",
        #     "Politik",
        #     "Politik"
        # ]
        
        # TF-IDF
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts)
        
        # Training
        model = RandomForestClassifier()
        model.fit(X, labels)
        
        # Testing
        # documents = [
        #     "Timnas lolos ke final",
        #     "IHSG mengalami kenaikan",
        #     "Presiden mengunjungi DPR"
        # ]

        # X_test = vectorizer.transform(documents)

        # predictions = model.predict(X_test)

        # for doc, label in zip(documents, predictions):
        #     print(doc, "->", label)
            
        model_klasifikasi = entity.ModelKlasifikasi(
            id=random.randint(1, 1000),
            nama="model1",
            algoritma="RandomForestClassifier",
            path="model1.joblib",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            model=model,
            is_trained=True
        )
        
        return model_klasifikasi
    
    
class VectorizerFactory:
    
    @staticmethod
    def create(texts: List[str]) -> entity.Vectorizer:
        # Dataset
        # texts = [
        #     "Timnas Indonesia menang",
        #     "Liga Champions dimulai",
        #     "Harga BBM naik",
        #     "Bursa saham menguat",
        #     "Presiden bertemu menteri",
        #     "DPR mengesahkan undang-undang"
        # ]
        
        model = TfidfVectorizer()
        model.fit(texts)
        
        hasil = entity.Vectorizer(
            id=random.randint(1, 1000),
            nama="vectorizer1",
            algoritma="TfidfVectorizer",
            path="vectorizer1.joblib",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            vectorizer=model,
            is_trained=True
        )
        
        return hasil