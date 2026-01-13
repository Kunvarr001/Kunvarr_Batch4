import requests
import json


class TumblrApiClient:
    def __init__(self, blog_name: str):
        # API endpoint is derived from the blog name to avoid hardcoding URLs
        self.api_url = f"https://{blog_name}.tumblr.com/api/read/json"

    def fetch_photo_posts(self) -> dict:
        response = requests.get(
            self.api_url,
            params={"type": "photo"},
            timeout=10
        )

        if response.status_code != 200:
            raise RuntimeError("Failed to fetch blog data")

        text = response.text

        # Tumblr API v1 wraps JSON inside JavaScript
        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1 or end == -1:
            raise RuntimeError("Invalid API response format")

        return json.loads(text[start:end])
