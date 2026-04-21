import pytest
from unittest.mock import patch, MagicMock
from tumblr_api_client import TumblrApiClient


class TestTumblrApiClient:

    @patch("tumblr_api_client.requests.get")
    def test_given_valid_response_when_fetching_then_returns_json(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = 'var tumblr_api_read = {"posts": []};'

        mock_get.return_value = mock_response

        client = TumblrApiClient("testblog")

        result = client.fetch_photo_posts()

        assert "posts" in result


    @patch("tumblr_api_client.requests.get")
    def test_given_failed_status_when_fetching_then_raises_exception(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response

        client = TumblrApiClient("testblog")

        with pytest.raises(RuntimeError):
            client.fetch_photo_posts()


    @patch("tumblr_api_client.requests.get")
    def test_given_invalid_response_when_fetching_then_raises_exception(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "invalid response"

        mock_get.return_value = mock_response

        client = TumblrApiClient("testblog")

        with pytest.raises(RuntimeError):
            client.fetch_photo_posts()