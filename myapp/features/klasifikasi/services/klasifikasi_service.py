from ..domain import vo, entity

class KlasifikasiService:
    def __init__(self, surat_repository, classifier: entity.ModelKlasifikasi, vectorizer: entity.Vectorizer) -> None:
        self.surat_repository = surat_repository
        self.classifier = classifier
        self.vectorizer = vectorizer
        
    def prediksi(self, surat: entity.Surat) -> vo.HasilKlasifikasi:
        X = self.vectorizer.vectorizer.transform([surat.isi])
        probabilitas = self.classifier.model.predict_proba([X])[0]
        classes = self.classifier.model.classes_
        
        index = probabilitas.argmax()
        
        hasil = vo.HasilKlasifikasi(
            label=classes[index],
            confidence=float(probabilitas[index]),
        )
        
        return hasil    

    def prediksi_banyak(self, surat_list: list[entity.Surat]) -> list[vo.HasilKlasifikasi]:
        documents = [
            surat.isi
            for surat in surat_list
        ]
        X = self.vectorizer.vectorizer.transform(documents)
        probabilities = self.model.predict_proba(X)

        classes = self.model.classes_

        hasil = []

        for probability in probabilities:
            index = probability.argmax()

            hasil.append(
                vo.HasilKlasifikasi(
                    label=classes[index],
                    confidence=float(probability[index])
                )
            )

        return hasil