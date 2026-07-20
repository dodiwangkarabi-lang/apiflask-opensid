from myapp.database.base_repository import BaseRepository

# model
from myapp.features.penduduk.models import TwebPenduduk, TwebKeluarga

class TwebPendudukRepository(BaseRepository[TwebPenduduk]):
    model = TwebPenduduk
    
class TwebKeluargaRepository(BaseRepository[TwebKeluarga]):
    model = TwebKeluarga