# from __future__ import annotations
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from myapp.features.auth.models.config_model import Config


# from datetime import date, datetime

# from sqlalchemy import Date, DateTime, ForeignKey, Integer, SmallInteger
# from sqlalchemy import String, Text, TIMESTAMP
# from sqlalchemy.dialects.mysql import TINYINT
# from sqlalchemy.orm import Mapped, mapped_column, relationship

# from myapp.extensions import db

# class TwebPenduduk(db.Model):
#     __tablename__ = "tweb_penduduk"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

#     config_id: Mapped[int] = mapped_column(
#         ForeignKey("config.id"),
#         nullable=False,
#     )

#     nama: Mapped[str] = mapped_column(String(100), nullable=False)
#     nik: Mapped[str | None] = mapped_column(String(16))
#     id_kk: Mapped[int | None] = mapped_column(ForeignKey("tweb_keluarga.id"))
#     kk_level: Mapped[int | None] = mapped_column(TINYINT)

#     id_rtm: Mapped[str | None] = mapped_column(String(30))
#     rtm_level: Mapped[int | None] = mapped_column(Integer)

#     sex: Mapped[int | None] = mapped_column(TINYINT(unsigned=True))
#     tempatlahir: Mapped[str | None] = mapped_column(String(100))
#     tanggallahir: Mapped[date] = mapped_column(Date, nullable=False)

#     agama_id: Mapped[int | None] = mapped_column(Integer)
#     pendidikan_kk_id: Mapped[int | None] = mapped_column(Integer)
#     pendidikan_sedang_id: Mapped[int | None] = mapped_column(Integer)
#     pekerjaan_id: Mapped[int | None] = mapped_column(Integer)

#     status_kawin: Mapped[int | None] = mapped_column(TINYINT)

#     warganegara_id: Mapped[int] = mapped_column(
#         TINYINT,
#         default=1,
#         nullable=False,
#     )

#     dokumen_pasport: Mapped[str | None] = mapped_column(String(45))
#     dokumen_kitas: Mapped[str | None] = mapped_column(String(45))

#     ayah_nik: Mapped[str | None] = mapped_column(String(16))
#     ibu_nik: Mapped[str | None] = mapped_column(String(16))

#     nama_ayah: Mapped[str | None] = mapped_column(String(100))
#     nama_ibu: Mapped[str | None] = mapped_column(String(100))

#     foto: Mapped[str | None] = mapped_column(String(100))

#     golongan_darah_id: Mapped[int | None] = mapped_column(Integer)
#     id_cluster: Mapped[int | None] = mapped_column(Integer)

#     status: Mapped[int | None] = mapped_column(Integer)

#     alamat_sebelumnya: Mapped[str | None] = mapped_column(String(200))
#     alamat_sekarang: Mapped[str | None] = mapped_column(String(200))

#     status_dasar: Mapped[int] = mapped_column(
#         TINYINT,
#         default=1,
#         nullable=False,
#     )

#     hamil: Mapped[int | None] = mapped_column(Integer)
#     cacat_id: Mapped[int | None] = mapped_column(Integer)
#     sakit_menahun_id: Mapped[int | None] = mapped_column(Integer)

#     akta_lahir: Mapped[str | None] = mapped_column(String(40))
#     akta_perkawinan: Mapped[str | None] = mapped_column(String(40))
#     tanggalperkawinan: Mapped[date | None] = mapped_column(Date)

#     akta_perceraian: Mapped[str | None] = mapped_column(String(40))
#     tanggalperceraian: Mapped[date | None] = mapped_column(Date)

#     cara_kb_id: Mapped[int | None] = mapped_column(TINYINT)

#     telepon: Mapped[str | None] = mapped_column(String(20))

#     tanggal_akhir_paspor: Mapped[date | None] = mapped_column(Date)

#     no_kk_sebelumnya: Mapped[str | None] = mapped_column(String(30))

#     ktp_el: Mapped[int | None] = mapped_column(TINYINT)
#     status_rekam: Mapped[int | None] = mapped_column(TINYINT)

#     waktu_lahir: Mapped[str | None] = mapped_column(String(5))

#     tempat_dilahirkan: Mapped[int | None] = mapped_column(TINYINT)
#     jenis_kelahiran: Mapped[int | None] = mapped_column(TINYINT)
#     kelahiran_anak_ke: Mapped[int | None] = mapped_column(TINYINT)
#     penolong_kelahiran: Mapped[int | None] = mapped_column(TINYINT)

#     berat_lahir: Mapped[int | None] = mapped_column(SmallInteger)
#     panjang_lahir: Mapped[str | None] = mapped_column(String(10))

#     tag_id_card: Mapped[str | None] = mapped_column(String(17))

#     id_asuransi: Mapped[int | None] = mapped_column(TINYINT)
#     no_asuransi: Mapped[str | None] = mapped_column(String(100))
#     status_asuransi: Mapped[int | None] = mapped_column(TINYINT)

#     email: Mapped[str | None] = mapped_column(String(100))
#     email_token: Mapped[str | None] = mapped_column(String(100))
#     email_tgl_kadaluarsa: Mapped[datetime | None] = mapped_column(DateTime)
#     email_tgl_verifikasi: Mapped[datetime | None] = mapped_column(DateTime)

#     telegram: Mapped[str | None] = mapped_column(String(100))
#     telegram_token: Mapped[str | None] = mapped_column(String(100))
#     telegram_tgl_kadaluarsa: Mapped[datetime | None] = mapped_column(DateTime)
#     telegram_tgl_verifikasi: Mapped[datetime | None] = mapped_column(DateTime)

#     bahasa_id: Mapped[int | None] = mapped_column(Integer)

#     ket: Mapped[str | None] = mapped_column(Text)

#     negara_asal: Mapped[str | None] = mapped_column(String(50))
#     tempat_cetak_ktp: Mapped[str | None] = mapped_column(String(150))
#     tanggal_cetak_ktp: Mapped[date | None] = mapped_column(Date)

#     suku: Mapped[str | None] = mapped_column(String(150))
#     marga: Mapped[str | None] = mapped_column(String(255))
#     adat: Mapped[str | None] = mapped_column(String(255))

#     bpjs_ketenagakerjaan: Mapped[str | None] = mapped_column(String(100))

#     hubung_warga: Mapped[str | None] = mapped_column(String(50))

#     created_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)
#     created_by: Mapped[int | None] = mapped_column(Integer)

#     updated_at: Mapped[datetime |None] = mapped_column(TIMESTAMP)
#     updated_by: Mapped[int | None] = mapped_column(Integer)
    
#     config: Mapped["Config"] = relationship(
#         back_populates="tweb_penduduk",
#     )

# ----- versi aman -----
from datetime import date, datetime

from sqlalchemy import (
    Date,
    DateTime,
    Integer,
    SmallInteger,
    String,
    Text,
    TIMESTAMP,
)
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column

from myapp.extensions import db


class TwebPenduduk(db.Model):
    __tablename__ = "tweb_penduduk"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # FK -> config.id
    config_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    nama: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    nik: Mapped[str | None] = mapped_column(
        String(16),
    )

    # FK -> tweb_keluarga.id
    id_kk: Mapped[int | None] = mapped_column(
        Integer,
    )

    kk_level: Mapped[int | None] = mapped_column(
        TINYINT,
    )

    id_rtm: Mapped[str | None] = mapped_column(
        String(30),
    )

    rtm_level: Mapped[int | None] = mapped_column(
        Integer,
    )

    sex: Mapped[int | None] = mapped_column(
        TINYINT(unsigned=True),
    )

    tempatlahir: Mapped[str | None] = mapped_column(
        String(100),
    )

    tanggallahir: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    agama_id: Mapped[int | None] = mapped_column(Integer)
    pendidikan_kk_id: Mapped[int | None] = mapped_column(Integer)
    pendidikan_sedang_id: Mapped[int | None] = mapped_column(Integer)
    pekerjaan_id: Mapped[int | None] = mapped_column(Integer)

    status_kawin: Mapped[int | None] = mapped_column(TINYINT)

    warganegara_id: Mapped[int] = mapped_column(
        TINYINT,
        default=1,
        nullable=False,
    )

    dokumen_pasport: Mapped[str | None] = mapped_column(String(45))
    dokumen_kitas: Mapped[str | None] = mapped_column(String(45))

    ayah_nik: Mapped[str | None] = mapped_column(String(16))
    ibu_nik: Mapped[str | None] = mapped_column(String(16))

    nama_ayah: Mapped[str | None] = mapped_column(String(100))
    nama_ibu: Mapped[str | None] = mapped_column(String(100))

    foto: Mapped[str | None] = mapped_column(String(100))

    golongan_darah_id: Mapped[int | None] = mapped_column(Integer)
    id_cluster: Mapped[int | None] = mapped_column(Integer)

    status: Mapped[int | None] = mapped_column(Integer)

    alamat_sebelumnya: Mapped[str | None] = mapped_column(String(200))
    alamat_sekarang: Mapped[str | None] = mapped_column(String(200))

    status_dasar: Mapped[int] = mapped_column(
        TINYINT,
        default=1,
        nullable=False,
    )

    hamil: Mapped[int | None] = mapped_column(Integer)
    cacat_id: Mapped[int | None] = mapped_column(Integer)
    sakit_menahun_id: Mapped[int | None] = mapped_column(Integer)

    akta_lahir: Mapped[str | None] = mapped_column(String(40))
    akta_perkawinan: Mapped[str | None] = mapped_column(String(40))
    tanggalperkawinan: Mapped[date | None] = mapped_column(Date)

    akta_perceraian: Mapped[str | None] = mapped_column(String(40))
    tanggalperceraian: Mapped[date | None] = mapped_column(Date)

    cara_kb_id: Mapped[int | None] = mapped_column(TINYINT)

    telepon: Mapped[str | None] = mapped_column(String(20))

    tanggal_akhir_paspor: Mapped[date | None] = mapped_column(Date)

    no_kk_sebelumnya: Mapped[str | None] = mapped_column(String(30))

    ktp_el: Mapped[int | None] = mapped_column(TINYINT)
    status_rekam: Mapped[int | None] = mapped_column(TINYINT)

    waktu_lahir: Mapped[str | None] = mapped_column(String(5))

    tempat_dilahirkan: Mapped[int | None] = mapped_column(TINYINT)
    jenis_kelahiran: Mapped[int | None] = mapped_column(TINYINT)
    kelahiran_anak_ke: Mapped[int | None] = mapped_column(TINYINT)
    penolong_kelahiran: Mapped[int | None] = mapped_column(TINYINT)

    berat_lahir: Mapped[int | None] = mapped_column(SmallInteger)
    panjang_lahir: Mapped[str | None] = mapped_column(String(10))

    tag_id_card: Mapped[str | None] = mapped_column(String(17))

    id_asuransi: Mapped[int | None] = mapped_column(TINYINT)
    no_asuransi: Mapped[str | None] = mapped_column(String(100))
    status_asuransi: Mapped[int | None] = mapped_column(TINYINT)

    email: Mapped[str | None] = mapped_column(String(100))
    email_token: Mapped[str | None] = mapped_column(String(100))
    email_tgl_kadaluarsa: Mapped[datetime | None] = mapped_column(DateTime)
    email_tgl_verifikasi: Mapped[datetime | None] = mapped_column(DateTime)

    telegram: Mapped[str | None] = mapped_column(String(100))
    telegram_token: Mapped[str | None] = mapped_column(String(100))
    telegram_tgl_kadaluarsa: Mapped[datetime | None] = mapped_column(DateTime)
    telegram_tgl_verifikasi: Mapped[datetime | None] = mapped_column(DateTime)

    bahasa_id: Mapped[int | None] = mapped_column(Integer)

    ket: Mapped[str | None] = mapped_column(Text)

    negara_asal: Mapped[str | None] = mapped_column(String(50))
    tempat_cetak_ktp: Mapped[str | None] = mapped_column(String(150))
    tanggal_cetak_ktp: Mapped[date | None] = mapped_column(Date)

    suku: Mapped[str | None] = mapped_column(String(150))
    marga: Mapped[str | None] = mapped_column(String(255))
    adat: Mapped[str | None] = mapped_column(String(255))

    bpjs_ketenagakerjaan: Mapped[str | None] = mapped_column(String(100))

    hubung_warga: Mapped[str | None] = mapped_column(String(50))

    created_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    created_by: Mapped[int | None] = mapped_column(Integer)

    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    updated_by: Mapped[int | None] = mapped_column(Integer)