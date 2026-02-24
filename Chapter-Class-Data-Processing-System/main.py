from file_data_source import FileDataSource
from delimited_record_parser import DelimitedRecordParser
from record_validator import RecordValidator
from record_transformer import RecordTransformer
from statistics_report_builder import StatisticsReportBuilder
from processing_journal import ProcessingJournal
from csv_result_writer import CsvResultWriter
from json_result_writer import JsonResultWriter
from data_processing_coordinator import DataProcessingCoordinator


def main():

    data_source = FileDataSource()
    parser = DelimitedRecordParser()
    validator = RecordValidator()
    transformer = RecordTransformer()
    statistics_builder = StatisticsReportBuilder()
    journal = ProcessingJournal()

    coordinator = DataProcessingCoordinator(
        data_source=data_source,
        parser=parser,
        validator=validator,
        transformer=transformer,
        statistics_builder=statistics_builder,
        journal=journal,
    )

    records, statistics = coordinator.execute("sample_input.csv")

    csv_writer = CsvResultWriter()
    json_writer = JsonResultWriter()

    csv_writer.write("output.csv", records, "%Y-%m-%d")
    json_writer.write("output.json", records, "%Y-%m-%d")

    journal.persist("processing.log")

    print("\nProcessing Statistics:")
    for key, value in statistics.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()