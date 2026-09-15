from dataclasses import dataclass

@dataclass
class Result:
    is_success: bool
    message: str
    data: any