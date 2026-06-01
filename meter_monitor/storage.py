import json
from datetime import date
from pathlib import Path

from meter_monitor.models import Reading


class JsonStorage:

    def __init__(self, filename: str) -> None:
        self.filename = Path(filename)

    def save(self, readings: list[Reading]) -> None:
        data = [{"meter_type": r.meter_type, 
                 "value": r.value, 
                 "date": str(r.date)} for r in readings]
        with open(self.filename, "w") as f:
                 json.dump(data, f)

                 
    def load(self) -> list[Reading]:
        if not self.filename.exists():
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
        return [Reading(
            meter_type=d["meter_type"], 
            value=d["value"], 
            date=date.fromisoformat(d["date"])) for d in data]
