import requests
import os
from libraries.validator import formatValidator

class Weather():
    def __init__(self):
        self.api_id     = os.environ.get("API_ID")
        self.url_format = os.environ.get("API_URL_FORMAT")
        self.session = requests.Session()

    def call_weather(self,city,country):
        api_consult     = self.url_format.format(city,country,self.api_id)
        status_code     = 404
        try:
            requested_data  = self.session.get(api_consult)
            status_code     = requested_data.status_code
        except Exception as e:
            response_data   = f"[Error] Error at calling external API {e}"
        
        if status_code!=200:
            response_data = "[Error] Error of extenal API."
        else:
            validator = formatValidator()
            response_data   = validator.format_response(requested_data.json())
        return response_data, status_code


