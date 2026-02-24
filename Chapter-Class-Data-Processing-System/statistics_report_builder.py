from data_record import DataRecord

class StatisticsReportBuilder:

    def build(self, records: list[DataRecord], error_count: int) -> dict:
        total_value = sum(record.value for record in records)

        return {
            "total_records": len(records),
            "error_count": error_count,
            "total_value": int(total_value),
            "average_value": int(total_value / len(records)) if records else 0,
        }