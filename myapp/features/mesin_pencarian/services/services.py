from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pickle
from pathlib import Path

from .utils import TextPreprocessor

class SearchEngine:
    def __init__(self, index_file: str = "index.pkl", file_location=None):
        self.index_file = Path(index_file)
        if file_location:
            self.index_file = Path(file_location)

        self.documents = []
        self.vectorizer = None
        self.tfidf_matrix = None
        self.inverted_index = {}

    def build(self, documents: list[dict], text_field: str):
        """
        Membangun index dari list dokumen.

        Args:
            documents: List data.
            text_field: Field yang akan digunakan untuk pencarian.
        """
        self.documents = documents

        corpus = [doc[text_field] for doc in documents]

        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)

        # Build inverted index
        self.inverted_index = {}

        for doc_id, text in enumerate(corpus):
            for token in text.lower().split():
                self.inverted_index.setdefault(token, set()).add(doc_id)

        self.save()

    def save(self):
        with open(self.index_file, "wb") as f:
            pickle.dump(
                {
                    "documents": self.documents,
                    "vectorizer": self.vectorizer,
                    "tfidf_matrix": self.tfidf_matrix,
                    "inverted_index": self.inverted_index,
                },
                f,
            )

    def load(self):
        with open(self.index_file, "rb") as f:
            data = pickle.load(f)

        self.documents = data["documents"]
        self.vectorizer = data["vectorizer"]
        self.tfidf_matrix = data["tfidf_matrix"]
        self.inverted_index = data["inverted_index"]

    def search(self, keyword: str, top_k: int = 20):
        """
        Melakukan pencarian menggunakan
        Inverted Index + Cosine Similarity.
        """

        # kandidat dokumen
        candidates = set()

        for token in keyword.lower().split():
            candidates |= self.inverted_index.get(token, set())

        if not candidates:
            return []

        query_vector = self.vectorizer.transform([keyword])

        candidate_ids = list(candidates)

        similarities = cosine_similarity(
            query_vector,
            self.tfidf_matrix[candidate_ids],
        )[0]

        results = sorted(
            zip(candidate_ids, similarities),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            {
                "score": float(score),
                "document": self.documents[idx],
            }
            for idx, score in results[:top_k]
        ]

class SearchEngine3:
    """
    Pencarian dengan algoritma
    
    params:
        items: List[Item]  
            -> item adalah instance surat (surat keluar atau surat masuk)
    """

    def __init__(self, items):
        self.items = items

        self.documents = [
            TextPreprocessor.preprocess(item.isi_singkat)
            for item in items
        ]

        self.vectorizer = TfidfVectorizer()
        self.document_vectors = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_k=5):
        """
        pencarian

        Args:
            query (str): kata kunci (keyword pencarian surat)
            top_k (int, optional): batas Jumlah hasil pencarian. Defaults to 5.

        Returns:
            tuple (surat, score): (surat: SuratKeluar | SuratMasuk, score: str | float)
        """
        query = TextPreprocessor.preprocess(query)

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        results = sorted(
            zip(self.items, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return results[:top_k]

class SearchEngineSurat:

    def __init__(self, items):
        self.items = items

        self.documents = [
            item.isi_singkat or ""
            for item in items
        ]

        self.vectorizer = TfidfVectorizer()
        self.document_vectors = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_k=5):
        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        results = sorted(
            zip(self.items, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return results[:top_k]


class SearchEngineFirst:

    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer()

        self.document_vectors = self.vectorizer.fit_transform(documents)

    def search(self, query, top_k=5):
        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        results = list(zip(self.documents, scores))

        results.sort(key=lambda x: x[1], reverse=True)

        return results[:top_k]
    
"""
contoh penggunaan



documents = [
    "Belajar Python untuk pemula",
    "Tutorial Flask menggunakan Python",
    "Belajar Machine Learning dengan Python",
    "Cara memasak nasi goreng"
]

engine = SearchEngine(documents)

hasil = engine.search("python flask")

for doc, score in hasil:
    print(score, doc)
    
"""