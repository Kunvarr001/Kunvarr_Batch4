import json
from data_record import DataRecord


class JsonResultWriter:

    def write(self, file_path: str, records: list[DataRecord], date_format: str):

        data = [record.to_serializable(date_format) for record in records]

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)