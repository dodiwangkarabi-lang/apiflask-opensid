


# ----- service -----
from myapp.features.mesin_pencarian.services import SearchEngine

# ----- repo -----

from myapp.config import BASE_DIR

INDEX_DIR = BASE_DIR / "media" / "index"

search_engine = SearchEngine(
    index_file = INDEX_DIR / "index.pkl"
)


class SearchEngineUseCase:
    def __init__(self, search_engine=search_engine):
        self.search_engine = search_engine
        
    def build(self, documents: list[dict], text_field: str):
        self.search_engine.build(documents, text_field)
    
    def search(self, keyword: str, top_k: int = 20) -> list[dict]:
        self.search_engine.load()
        
        return self.search_engine.search(keyword)