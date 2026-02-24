class DataProcessingCoordinator:

    def __init__(self,data_source,parser,validator,transformer,statistics_builder,journal,):
        self.data_source = data_source
        self.parser = parser
        self.validator = validator
        self.transformer = transformer
        self.statistics_builder = statistics_builder
        self.journal = journal

    def execute(self, input_path: str):
        self.journal.record("Starting processing")
        lines = self.data_source.read_lines(input_path)
        records, parse_errors = self.parser.parse(lines)
        records, validation_errors = self.validator.validate(records)
        records = self.transformer.transform(records)
        total_errors = len(parse_errors) + len(validation_errors)
        statistics = self.statistics_builder.build(records, total_errors)
        self.journal.record("Processing completed")

        return records, statistics