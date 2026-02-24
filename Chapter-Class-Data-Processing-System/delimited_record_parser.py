from datetime import datetime
from data_record import DataRecord


class DelimitedRecordParser:

    def parse(self, lines: list[str]) -> tuple[list[DataRecord], list[str]]:
        records = []
        errors = []

        for line in lines:
            clean_line = line.strip()
            if not clean_line:
                continue

            parts = clean_line.split(",")

            if len(parts) < 3:
                errors.append(f"Invalid line format: {clean_line}")
                continue

            try:
                identifier = parts[0].strip()
                name = parts[1].strip()
                value = float(parts[2].strip())

                date = None
                if len(parts) >= 4:
                    date = datetime.strptime(parts[3].strip(), "%Y-%m-%d")

                records.append(DataRecord(identifier, name, value, date))

            except Exception as ex:
                errors.append(f"Parsing error: {clean_line} | {ex}")

        return records, errors