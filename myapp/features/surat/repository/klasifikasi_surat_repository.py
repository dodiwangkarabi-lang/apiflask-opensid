from myapp.core import BaseRepository
from myapp.features.surat import models

class KlasifikasiSuratRepository(BaseRepository[models.SuratMasuk]):
    model = models.KlasifikasiSurat