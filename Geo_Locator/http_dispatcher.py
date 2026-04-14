import requests

class HttpDispatcher:
    def get(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Unable to establish a connection with the geocoding service")
        return response.json()