from data_record import DataRecord

class RecordTransformer:

    def transform(self, records: list[DataRecord]) -> list[DataRecord]:

        for record in records:
            record.name = record.name.upper()

        return records