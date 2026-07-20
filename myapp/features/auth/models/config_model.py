# # config/models.py
# from __future__ import annotations
# from typing import TYPE_CHECKING

# from datetime import datetime

# from sqlalchemy import (
#     Integer,
#     String,
#     Text,
#     DateTime,
# )

# from sqlalchemy.orm import Mapped, mapped_column, relationship

# from myapp.extensions import db

# if TYPE_CHECKING:
#     from myapp.features.auth.models.user_model import User
    
#     # ----- models -----
#     from myapp.features.penduduk.models import (
#         TwebKeluarga, TwebPenduduk
#     )
#     from myapp.features.surat.models import (
#         SuratKeluar, SuratMasuk
#     )

# class Config(db.Model):
#     __tablename__ = "config"

#     id: Mapped[int] = mapped_column(
#         Integer,
#         primary_key=True,
#     )

#     app_key: Mapped[str] = mapped_column(
#         String(100),
#         unique=True,
#         nullable=False,
#     )

#     nama_desa: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     kode_desa: Mapped[str | None] = mapped_column(
#         String(10),
#         unique=True,
#     )

#     kode_desa_bps: Mapped[str | None] = mapped_column(
#         String(10),
#     )

#     kode_pos: Mapped[int | None] = mapped_column(
#         Integer,
#     )

#     nama_kecamatan: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     kode_kecamatan: Mapped[str | None] = mapped_column(
#         String(6),
#     )

#     nama_kepala_camat: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     nip_kepala_camat: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     nama_kabupaten: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     kode_kabupaten: Mapped[str | None] = mapped_column(
#         String(4),
#     )

#     nama_propinsi: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     kode_propinsi: Mapped[str | None] = mapped_column(
#         String(2),
#     )

#     logo: Mapped[str | None] = mapped_column(
#         String(100),
#     )

#     lat: Mapped[str | None] = mapped_column(
#         String(20),
#     )

#     lng: Mapped[str | None] = mapped_column(
#         String(20),
#     )

#     zoom: Mapped[int | None] = mapped_column(
#         Integer,
#     )

#     map_tipe: Mapped[str | None] = mapped_column(
#         String(20),
#     )

#     path: Mapped[str | None] = mapped_column(
#         Text,
#     )

#     alamat_kantor: Mapped[str | None] = mapped_column(
#         String(200),
#     )

#     email_desa: Mapped[str | None] = mapped_column(
#         String(100),
#     )

#     telepon: Mapped[str | None] = mapped_column(
#         String(50),
#     )

#     nomor_operator: Mapped[str | None] = mapped_column(
#         String(20),
#     )

#     website: Mapped[str | None] = mapped_column(
#         String(100),
#     )

#     kantor_desa: Mapped[str | None] = mapped_column(
#         String(100),
#     )

#     warna: Mapped[str | None] = mapped_column(
#         String(25),
#     )

#     border: Mapped[str | None] = mapped_column(
#         String(25),
#     )

#     created_at: Mapped[datetime | None] = mapped_column(
#         DateTime,
#     )

#     created_by: Mapped[int | None] = mapped_column(
#         Integer,
#     )

#     updated_at: Mapped[datetime | None] = mapped_column(
#         DateTime,
#     )

#     updated_by: Mapped[int | None] = mapped_column(
#         Integer,
#     )

#     nama_kontak: Mapped[str | None] = mapped_column(
#         String(80),
#     )

#     hp_kontak: Mapped[str | None] = mapped_column(
#         String(20),
#     )

#     jabatan_kontak: Mapped[str | None] = mapped_column(
#         String(80),
#     )
    
#     users: Mapped[list["User"]] = relationship(
#         back_populates="config"
#     )
    
#     tweb_penduduk: Mapped[list["TwebPenduduk"]] = relationship(
#         back_populates="config"
#     )
    
#     tweb_keluarga: Mapped[list["TwebKeluarga"]] = relationship(
#         back_populates="config"
#     )
    
#     surat_keluar: Mapped[list["SuratKeluar"]] = relationship(
#         back_populates="config",
#         cascade="all, delete-orphan",
#     )
    
#     surat_masuk: Mapped[list["SuratMasuk"]] = relationship(
#         back_populates="config",
#         cascade="all, delete-orphan",
#     )

# ----- versi aman -----
from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column

from myapp.extensions import db


class Config(db.Model):
    __tablename__ = "config"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    app_key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    nama_desa: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    kode_desa: Mapped[str | None] = mapped_column(
        String(10),
        unique=True,
    )

    kode_desa_bps: Mapped[str | None] = mapped_column(
        String(10),
    )

    kode_pos: Mapped[int | None] = mapped_column(
        Integer,
    )

    nama_kecamatan: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    kode_kecamatan: Mapped[str | None] = mapped_column(
        String(6),
    )

    nama_kepala_camat: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    nip_kepala_camat: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    nama_kabupaten: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    kode_kabupaten: Mapped[str | None] = mapped_column(
        String(4),
    )

    nama_propinsi: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    kode_propinsi: Mapped[str | None] = mapped_column(
        String(2),
    )

    logo: Mapped[str | None] = mapped_column(
        String(100),
    )

    lat: Mapped[str | None] = mapped_column(
        String(20),
    )

    lng: Mapped[str | None] = mapped_column(
        String(20),
    )

    zoom: Mapped[int | None] = mapped_column(
        Integer,
    )

    map_tipe: Mapped[str | None] = mapped_column(
        String(20),
    )

    path: Mapped[str | None] = mapped_column(
        Text,
    )

    alamat_kantor: Mapped[str | None] = mapped_column(
        String(200),
    )

    email_desa: Mapped[str | None] = mapped_column(
        String(100),
    )

    telepon: Mapped[str | None] = mapped_column(
        String(50),
    )

    nomor_operator: Mapped[str | None] = mapped_column(
        String(20),
    )

    website: Mapped[str | None] = mapped_column(
        String(100),
    )

    kantor_desa: Mapped[str | None] = mapped_column(
        String(100),
    )

    warna: Mapped[str | None] = mapped_column(
        String(25),
    )

    border: Mapped[str | None] = mapped_column(
        String(25),
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    created_by: Mapped[int | None] = mapped_column(
        Integer,
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    updated_by: Mapped[int | None] = mapped_column(
        Integer,
    )

    nama_kontak: Mapped[str | None] = mapped_column(
        String(80),
    )

    hp_kontak: Mapped[str | None] = mapped_column(
        String(20),
    )

    jabatan_kontak: Mapped[str | None] = mapped_column(
        String(80),
    )