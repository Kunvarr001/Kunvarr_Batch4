from data_record import DataRecord

class CsvResultWriter:

    def write(self, file_path: str, records: list[DataRecord], date_format: str):
        with open(file_path, "w") as file:
            file.write("ID,NAME,VALUE,DATE,DOUBLED_VALUE,SQUARED_VALUE\n")

            for record in records:
                data = record.to_serializable(date_format)
                row = ",".join(str(value) for value in data.values())
                file.write(row + "\n")