from dataclasses import dataclass

from myapp.config import BASE_DIR

# ----- service -----
from myapp.features.mesin_pencarian.services import SearchEngine

# ----- repository -----
from myapp.features.surat import repository

INDEX_DIR = BASE_DIR / "media" / "index"

@dataclass(frozen=True)
class SearchModel:
    search_engine: SearchEngine
    repo: object
    
MODEL_PENCARIAN_SURAT_KELUAR = SearchModel(
    search_engine=SearchEngine(index_file=INDEX_DIR / "index_surat_keluar.pkl"),
    repo=repository.SuratKeluarRepository()
)

MODEL_PENCARIAN_SURAT_MASUK = SearchModel(
    search_engine=SearchEngine(index_file=INDEX_DIR / "index_surat_masuk.pkl"),
    repo=repository.SuratMasukRepository()
)

"""
Usage:

MODEL_PENCARIAN_SURAT_KELUAR.repo
MODEL_PENCARIAN_SURAT_KELUAR.search_engine
"""

# MODEL_PENCARIAN_SURAT_KELUAR = {
#     "search_engine": SearchEngine(
#         index_file=INDEX_DIR / "index_surat_keluar.pkl"
#     ),
#     "repo": repository.SuratKeluarRepository()
# }

# MODEL_PENCARIAN_SURAT_MASUK = {
#     "search_engine": SearchEngine(
#         index_file=INDEX_DIR / "index_surat_masuk.pkl"
#     ),
#     "repo": repository.SuratMasukRepository()
# }