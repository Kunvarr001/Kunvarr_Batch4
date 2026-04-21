import pytest
from unittest.mock import patch
from opencage_geo_gateway import OpenCageGeoGateway


class TestOpenCageGeoGateway:

    @patch("opencage_geo_gateway.requests.get")
    def test_given_valid_location_when_called_then_returns_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": []}

        gateway = OpenCageGeoGateway("fake_key")

        result = gateway.retrieve("Delhi")

        assert "results" in result


    @patch("opencage_geo_gateway.requests.get")
    def test_given_api_failure_when_called_then_raises_exception(self, mock_get):
        mock_get.return_value.status_code = 500

        gateway = OpenCageGeoGateway("fake_key")

        with pytest.raises(Exception):
            gateway.retrieve("Delhi")


    @patch("opencage_geo_gateway.requests.get")
    def test_given_network_error_when_called_then_raises_exception(self, mock_get):
        mock_get.side_effect = Exception("Network error")

        gateway = OpenCageGeoGateway("fake_key")

        with pytest.raises(Exception):
            gateway.retrieve("Delhi")