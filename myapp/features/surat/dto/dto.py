from dataclasses import dataclass, field
from typing import Optional
import random
from datetime import date, datetime, time

@dataclass
class SuratDTO:
    id: int
    tanggal_surat: date

    config_id: Optional[int] = None
    nomor_urut: Optional[int] = None
    nomor_surat: Optional[str] = None
    kode_surat: Optional[str] = None
    isi_singkat: Optional[str] = None
    berkas_scan: Optional[str] = None
    lokasi_arsip: str = ""

@dataclass
class SuratKeluarDTO:
    id: int
    tanggal_surat: date

    config_id: Optional[int] = None
    nomor_urut: Optional[int] = None
    nomor_surat: Optional[str] = None
    kode_surat: Optional[str] = None
    tanggal_catat: Optional[datetime] = None
    tujuan: Optional[str] = None
    isi_singkat: Optional[str] = None
    berkas_scan: Optional[str] = None
    ekspedisi: int = 0
    tanggal_pengiriman: Optional[date] = None
    tanda_terima: Optional[str] = None
    keterangan: Optional[str] = None
    lokasi_arsip: str = ""
    created_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None

@dataclass
class SuratMasukDTO:
    id: int
    tanggal_penerimaan: date
    tanggal_surat: date

    config_id: Optional[int] = None
    nomor_urut: Optional[int] = None
    nomor_surat: Optional[str] = None
    kode_surat: Optional[str] = None
    pengirim: Optional[str] = None
    isi_singkat: Optional[str] = None
    isi_disposisi: Optional[str] = None
    berkas_scan: Optional[str] = None
    lokasi_arsip: str = ""


@dataclass
class SuratMasukRequest:
    nomor_urut: int
    kode_surat: str
    nomor_surat: str
    tanggal_surat: str
    # tujuan: str
    isi_singkat: str
    berkas_scan: str
    
    # id: int = field(default_factory=lambda: random.randint(1, 100))
    config_id: int = 1
    isi_disposisi: str = None
    pengirim: str = None
    tanggal_penerimaan: str = None
    lokasi_arsip: str = None