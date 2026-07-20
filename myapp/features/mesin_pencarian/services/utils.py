import re

# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


# class TextPreprocessor:

#     stemmer = StemmerFactory().create_stemmer()
#     stopword = StopWordRemoverFactory().create_stop_word_remover()

#     @classmethod
#     def preprocess(cls, text: str | None) -> str:
#         if not text:
#             return ""

#         text = text.lower()
#         text = re.sub(r"[^a-zA-Z\s]", " ", text)
#         text = re.sub(r"\s+", " ", text).strip()

#         text = cls.stopword.remove(text)
#         text = cls.stemmer.stem(text)

#         return text


class TextPreprocessor:

    @staticmethod
    def preprocess(text: str | None) -> str:
        if not text:
            return ""

        # lowercase
        text = text.lower()
        
        # Sisakan hanya huruf dan spasi
        text = re.sub(r"[^a-z\s]", " ", text)

        # hapus karakter selain huruf, angka, dan spasi
        # text = re.sub(r"[^a-z0-9\s]", " ", text)

        # hapus spasi berlebih
        text = re.sub(r"\s+", " ", text).strip()

        return text