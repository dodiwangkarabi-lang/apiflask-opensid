from myapp.core import BaseRepository
from myapp.features.surat import models


class SuratMasukRepository(BaseRepository[models.SuratMasuk]):
    model = models.SuratMasuk
    

class SuratKeluarRepository(BaseRepository[models.SuratKeluar]):
    model = models.SuratKeluar