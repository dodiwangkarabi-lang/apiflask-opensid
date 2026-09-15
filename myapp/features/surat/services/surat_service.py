from ..models import SuratKeluar, SuratMasuk
from ..repository import SuratRepository, SuratKeluarRepository, SuratMasukRepository

from myapp.extensions import db
session = db.session

# ----- dto -----
from myapp.features.shared.dto import dto
from myapp.features.surat import dto as dto_surat_masuk


class SuratService:
    def __init__(self, surat_repository: SuratRepository):
        self.surat_repository = surat_repository
        
    def get_all(self) -> list[SuratKeluar | SuratMasuk]:
        return self.surat_repository.get_all()
    
    def get_by_id(self, id: int, jenis="surat_masuk") -> SuratMasuk | SuratKeluar:
        return self.surat_repository.get_by_id(id, jenis)
    

# ----- surat base repository -----
class SuratBaseService:
    def __init__(self, surat_repository):
        self.surat_repository = surat_repository
        
    def create(self, **kwargs) -> dto.Result:
        session = self.surat_repository.session
        try:
            obj = self.surat_repository.tambah(**kwargs)
            session.commit()
            
            return dto.Result(data=obj, is_success=True, message="Surat masuk berhasil ditambahkan")
        except Exception as e:
            session.rollback()
            
            return dto.Result(data=None, is_success=False, message=str(e))
        finally:
            pass
            # session.close()
                    
    def edit(self, id: int, **kwargs) -> dto.Result:
        session = self.surat_repository.session

        try:
            obj = self.surat_repository.edit(id, **kwargs)

            if obj is None:
                return dto.Result(
                    data=None,
                    is_success=False,
                    message="Surat masuk tidak ditemukan"
                )

            session.commit()

            return dto.Result(
                data=obj,
                is_success=True,
                message="Surat masuk berhasil diubah"
            )

        except Exception as e:
            session.rollback()

            return dto.Result(
                data=None,
                is_success=False,
                message=str(e)
            )

        finally:
            pass
            # session.close()
    
    def hapus(self, id: int) -> dto.Result:
        session = self.surat_repository.session

        try:
            obj = self.surat_repository.hapus(id)

            if obj is None:
                return dto.Result(
                    data=None,
                    is_success=False,
                    message="Surat masuk tidak ditemukan"
                )

            session.commit()

            return dto.Result(
                data=None,
                is_success=True,
                message="Surat masuk berhasil dihapus"
            )

        except Exception as e:
            session.rollback()

            return dto.Result(
                data=None,
                is_success=False,
                message=str(e)
            )

        finally:
            pass
            # session.close()
    
    def lihat(self, id: int) -> dto.Result:
        session = self.surat_repository.session
        try:
            obj = self.surat_repository.lihat(id)
            if obj is None:
                return dto.Result(
                    data=None,
                    is_success=False,
                    message="Surat masuk tidak ditemukan"
                )
            return dto.Result(data=obj, is_success=True, message="Surat masuk berhasil dilihat")
        except Exception as e:
            return dto.Result(data=None, is_success=False, message=str(e))
        finally:
            pass
            # session.close()
    
    def semua_surat(self) -> dto.Result:
        try:
            obj = self.surat_repository.lihat_semua()

            return dto.Result(
                data=obj,
                is_success=True,
                message="Semua surat masuk berhasil dilihat"
            )

        except Exception as e:
            return dto.Result(
                data=None,
                is_success=False,
                message=str(e)
            )

        finally:
            pass
            # self.surat_repository.session.close()
        

session = db.session
surat_masuk_service = SuratBaseService(SuratMasukRepository(session=session))
surat_keluar_service = SuratBaseService(SuratKeluarRepository(session=session))

# class SuratKeluarService:
#     def __init__(self, surat_repository: SuratKeluarRepository = SuratKeluarRepository()):
#         self.surat_repository = surat_repository
            
#     def create(self, **kwargs) -> dto.Result:
#         obj = self.surat_repository.tambah(**kwargs)
#         return dto.Result(data=obj, is_success=True, message="Surat keluar berhasil ditambahkan")
        
#     def edit(self, id: int, **kwargs) -> dto.Result:
#         try:
#             obj = self.surat_repository.edit(id, **kwargs)
#             return dto.Result(data=obj, is_success=True, message="Surat keluar berhasil diedit")
#         except Exception as e:
#             return dto.Result(data=None, is_success=False, message="Surat keluar gagal diedit")
    
#     def hapus(self, id: int) -> dto.Result:
#         self.surat_repository.hapus(id)
#         return dto.Result(data=None, is_success=True, message="Surat keluar berhasil dihapus")
    
#     def lihat(self, id: int) -> dto.Result:
#         obj = self.surat_repository.lihat(id)
#         if obj is None:
#             return dto.Result(data=None, is_success=False, message="Surat keluar tidak ditemukan")
#         return dto.Result(data=obj, is_success=True, message="Surat keluar berhasil dilihat")
    
#     def semua_surat(self) -> dto.Result:
#         obj = self.surat_repository.lihat_semua()
#         return dto.Result(data=obj, is_success=True, message="Semua surat keluar berhasil dilihat")