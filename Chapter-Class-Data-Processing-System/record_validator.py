from data_record import DataRecord

class RecordValidator:

    def validate(self, records: list[DataRecord]) -> tuple[list[DataRecord], list[str]]:
        valid_records = []
        errors = []

        for record in records:
            if not record.identifier:
                errors.append("Record missing identifier")
                continue

            if not record.name:
                errors.append(f"Record {record.identifier} missing name")
                continue

            valid_records.append(record)

        return valid_records, errors