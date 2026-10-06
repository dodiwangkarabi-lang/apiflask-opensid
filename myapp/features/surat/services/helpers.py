from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

from dataclasses import dataclass
# import typing

@dataclass
class DatasetTyping:
    id: int
    isi_singkat: str
    kode_surat: str


def latih_model(*, media_root, simpan=False, dataset: list[DatasetTyping]=None):
    """

    Args:
        media_root (_type_): _description_
        simpan (bool, optional): _description_. Defaults to False.
        dataset (list[DatasetTyping], optional): adalah instance dari list[semua data]. Defaults to None.

    Raises:
        Exception: _description_
    """
    if dataset is None:
        raise Exception("Dataset harus diisi")
    
    # data yang digunakan
    X_train = []
    y_train = []
    document_ids = []
    for value in dataset:
        X_train.append(value.isi_singkat)
        y_train.append(value.kode_surat)
        document_ids.append(value.id)
    
    # X_train = dataset["isi_singkat"]
    # y_train = dataset["kode_surat"]
    # document_ids = [
    #     value["id"]
    #     for value in dataset
    # ]
    
    model = Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            ngram_range=(1, 1),
            max_features=5000
        )),
        ("classifier", RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            criterion="gini"
        ))
    ])
    
    model.fit(X_train, y_train)
    
    vectorizer = model.named_steps["tfidf"]
    # classifier = model.named_steps["classifier"]
    
    X_database = vectorizer.transform(X_train)
    
    if simpan:
        path_model = media_root / "model"

        # simpan model pipeline
        joblib.dump(model, path_model / "model_klasifikasi.joblib")
        
        # simpan artifact
        artifact = {
            "vectorizer": vectorizer,
            "matrix": X_database,
            "document_ids": document_ids
        }
        joblib.dump(artifact, path_model / "vectorizer.joblib")
        