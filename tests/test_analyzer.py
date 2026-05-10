from datetime import date
from meter_monitor.models import Reading
import pytest
from meter_monitor.analyzer import Analyzer 


def test_calculate_consumption():
    readings = [
            Reading(meter_type="electricity", value=100.0, date=date(2026,4,10)),
            Reading(meter_type="electricity", value=150.0, date=date(2026,5,10)),
    ]

    analyzer = Analyzer()
    result = analyzer.calculate_consumption(readings)
    assert result[0]["consumption"] == 50.0    






