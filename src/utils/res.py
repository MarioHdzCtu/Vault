from dataclasses import dataclass

@dataclass
class Res:
    msg: str
    status_code: int
    data: list | dict | None = None