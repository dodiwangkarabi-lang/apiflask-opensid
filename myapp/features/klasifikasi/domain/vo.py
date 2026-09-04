from dataclasses import dataclass

# value object
@dataclass
class HasilKlasifikasi:
    label: str
    confidence: float | None