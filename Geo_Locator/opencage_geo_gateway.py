import requests

class OpenCageGeoGateway:
    def __init__(self, api_key):
        self.api_key = api_key

    def retrieve(self, location):
        url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={self.api_key}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Unable to retrieve location data due to a connection issue.")

        return response.json()