# from __future__ import annotations
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from myapp.features.auth.models.config_model import Config

# from datetime import date

# from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String
# from sqlalchemy.orm import Mapped, mapped_column, relationship

# from myapp.extensions import db


# class SuratMasuk(db.Model):
#     __tablename__ = "surat_masuk"

#     id: Mapped[int] = mapped_column(
#         Integer,
#         primary_key=True,
#         autoincrement=True,
#     )

#     config_id: Mapped[int | None] = mapped_column(
#         ForeignKey("config.id"),
#         nullable=True,
#         index=True,
#     )

#     nomor_urut: Mapped[int | None] = mapped_column(
#         SmallInteger,
#         nullable=True,
#     )

#     tanggal_penerimaan: Mapped[date] = mapped_column(
#         Date,
#         nullable=False,
#     )

#     nomor_surat: Mapped[str | None] = mapped_column(
#         String(35),
#         nullable=True,
#     )

#     kode_surat: Mapped[str | None] = mapped_column(
#         String(10),
#         nullable=True,
#     )

#     tanggal_surat: Mapped[date] = mapped_column(
#         Date,
#         nullable=False,
#     )

#     pengirim: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     isi_singkat: Mapped[str | None] = mapped_column(
#         String(200),
#         nullable=True,
#     )

#     isi_disposisi: Mapped[str | None] = mapped_column(
#         String(200),
#         nullable=True,
#     )

#     berkas_scan: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     lokasi_arsip: Mapped[str | None] = mapped_column(
#         String(150),
#         nullable=True,
#         server_default="",
#     )

#     # Relationship
#     config: Mapped["Config | None"] = relationship(
#         back_populates="surat_masuk"
#     )

# ----- versi aman -----
from datetime import date

from sqlalchemy import (
    Date,
    Integer,
    SmallInteger,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from myapp.extensions import db


class SuratMasuk(db.Model):
    __tablename__ = "surat_masuk"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # FK -> config.id
    config_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
        index=True,
    )

    nomor_urut: Mapped[int | None] = mapped_column(
        SmallInteger,
        nullable=True,
    )

    tanggal_penerimaan: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    nomor_surat: Mapped[str | None] = mapped_column(
        String(35),
        nullable=True,
    )

    kode_surat: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    tanggal_surat: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    pengirim: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    isi_singkat: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    isi_disposisi: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    berkas_scan: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    lokasi_arsip: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        server_default="",
    )