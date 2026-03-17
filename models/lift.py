from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Lift:
    id: str
    liftType: str # GONDOLA, CHAIRLIFT
    definition: str # REGULAR, TRANSIT  (TRANSIT = Talstation)
    startTime: int
    endTime: int
    duration: int
    waitingTime: int
    

    
