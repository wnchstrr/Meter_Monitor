from dataclasses import dataclass
from datetime import date


@dataclass
class Reading:
    meter_type: str 
    value: float
    date: date
