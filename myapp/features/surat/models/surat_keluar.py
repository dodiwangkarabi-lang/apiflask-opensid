# from __future__ import annotations
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from myapp.features.auth.models.config_model import Config

# from datetime import date, datetime

# from sqlalchemy import Date, DateTime, ForeignKey, Integer, SmallInteger, String
# from sqlalchemy.dialects.mysql import TIMESTAMP, TINYINT
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy.sql import func

# from myapp.extensions import db


# class SuratKeluar(db.Model):
#     __tablename__ = "surat_keluar"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

#     config_id: Mapped[int | None] = mapped_column(
#         ForeignKey("config.id"),
#         nullable=True,
#         index=True,
#     )

#     nomor_urut: Mapped[int | None] = mapped_column(
#         SmallInteger,
#         nullable=True,
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

#     tanggal_catat: Mapped[datetime] = mapped_column(
#         TIMESTAMP,
#         server_default=func.current_timestamp(),
#         nullable=False,
#     )

#     tujuan: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     isi_singkat: Mapped[str | None] = mapped_column(
#         String(200),
#         nullable=True,
#     )

#     berkas_scan: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     ekspedisi: Mapped[bool] = mapped_column(
#         TINYINT(1),
#         nullable=True,
#         server_default="0",
#     )

#     tanggal_pengiriman: Mapped[date | None] = mapped_column(
#         Date,
#         nullable=True,
#     )

#     tanda_terima: Mapped[str | None] = mapped_column(
#         String(200),
#         nullable=True,
#     )

#     keterangan: Mapped[str | None] = mapped_column(
#         String(500),
#         nullable=True,
#     )

#     lokasi_arsip: Mapped[str | None] = mapped_column(
#         String(150),
#         nullable=True,
#         server_default="",
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         TIMESTAMP,
#         nullable=True,
#         server_default=func.current_timestamp(),
#     )

#     created_by: Mapped[int | None] = mapped_column(
#         Integer,
#         nullable=True,
#     )

#     updated_at: Mapped[datetime] = mapped_column(
#         TIMESTAMP,
#         nullable=True,
#         server_default=func.current_timestamp(),
#         server_onupdate=func.current_timestamp(),
#     )

#     updated_by: Mapped[int | None] = mapped_column(
#         Integer,
#         nullable=True,
#     )

#     # Relationship
#     config: Mapped["Config | None"] = relationship(
#         back_populates="surat_keluar"
#     )

# ----- versi aman -----
from datetime import date, datetime

from sqlalchemy import (
    Date,
    Integer,
    SmallInteger,
    String,
)
from sqlalchemy.dialects.mysql import TIMESTAMP, TINYINT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from myapp.extensions import db


class SuratKeluar(db.Model):
    __tablename__ = "surat_keluar"

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

    tanggal_catat: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
    )

    tujuan: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    isi_singkat: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    berkas_scan: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    ekspedisi: Mapped[bool] = mapped_column(
        TINYINT(1),
        nullable=True,
        server_default="0",
    )

    tanggal_pengiriman: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    tanda_terima: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    keterangan: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    lokasi_arsip: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        server_default="",
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=True,
        server_default=func.current_timestamp(),
    )

    created_by: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=True,
        server_default=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
    )

    updated_by: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )