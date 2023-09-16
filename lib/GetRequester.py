import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                return response.json()
            except ValueError as e:
                print(f"Error parsing JSON: {e}")
                return None

