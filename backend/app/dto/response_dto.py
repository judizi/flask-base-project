from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ResponseDTO:
    code: int
    message: str
    data: Optional[Any] = None

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }
    
