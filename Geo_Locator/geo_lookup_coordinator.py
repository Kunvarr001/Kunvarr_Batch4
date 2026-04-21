from input_screener import InputScreener
from opencage_geo_gateway import OpenCageGeoGateway
from geo_result_translator import GeoResultTranslator
from output_presenter import OutputPresenter
from fault_reporter import FaultReporter

class GeoLookupCoordinator:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.validator = InputScreener()
        self.gateway = OpenCageGeoGateway(self.api_key)
        self.translator = GeoResultTranslator()
        self.presenter = OutputPresenter()
        self.error_handler = FaultReporter()

    def process(self, location_text):
        if not self.validator.is_valid(location_text):
            self.error_handler.show("Invalid location input")
            return

        try:
            raw_data = self.gateway.retrieve(location_text)
            records = self.translator.transform(raw_data)
            self.presenter.render(records)
        except Exception as ex:
            self.error_handler.show(str(ex))