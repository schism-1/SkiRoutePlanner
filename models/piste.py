from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Piste:
    id: str
    difficulty: str # BLUE, RED, BLACK
    surface: str # NORMAL, ICY, BUMPY
    length: int
    altitudeDiff: int

    @classmethod
    def slope(cls, altitude_diff: int, length: int):
        if length == 0:
            return 0
        return altitude_diff / length

    
