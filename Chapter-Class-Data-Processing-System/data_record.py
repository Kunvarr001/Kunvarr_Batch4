from dataclasses import dataclass
from datetime import datetime

@dataclass
class DataRecord:
    identifier: str
    name: str
    value: float
    date: datetime | None = None

    def to_serializable(self, date_format: str) -> dict:
        return {
            "id": self.identifier,
            "name": self.name,
            "value": self.value,
            "date": self.date.strftime(date_format) if self.date else "",
            "doubled_value": self.value * 2,
            "squared_value": self.value ** 2,
        }