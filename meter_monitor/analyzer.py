from meter_monitor.models import Reading


class Analyzer:

    def calculate_consumption(self, readings: list[Reading]) -> list[dict]:
        result = []
        for i in range(1, len(readings)):
            current = readings[i]
            previous = readings[i -1]
            consumption = current.value - previous.value
            result.append({
                "date": current.date,
                "meter_type": current.meter_type,
                "consumption": consumption, 
            })
        return result 
