from .base import ModelRepositoryBase
from ..domain import entity

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / "media"

class ModelRepositoryImpl(ModelRepositoryBase):
    def __init__(self, media_root: Path = MEDIA_ROOT) -> None:
        self.media_root = media_root
        
    def save(self, data: entity.ModelKlasifikasi, nama_model: str = "") -> None:
        """

        Args:
            data (entity.ModelKlasifikasi): _description_
            nama_model (str, optional): _description_. Defaults to "".
            
        Example:
            >>> data = entity.ModelKlasifikasi()
            >>> data.model = model
            >>> data.nama = "model1"
            >>> repository.save(data, "model1.joblib")
        """
        if not nama_model:
            nama_model = data.nama
        joblib.dump(data.model, self.media_root / nama_model)
    
    def load(self, nama_model: str) -> entity.ModelKlasifikasi:
        """

        Args:
            nama_model (str): contoh: model1.joblib

        Returns:
            entity.ModelKlasifikasi: _description_
            
        Example:
            >>> repository.load("model1.joblib")
        """

        result = joblib.load(self.media_root / nama_model)
        
        return result