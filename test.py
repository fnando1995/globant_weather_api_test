import unittest
import requests
import os
from libraries.weather import *

class test_weather(unittest.TestCase):

    def test_format_validations(self):
        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("guayaquil","ecc"))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] country argument should be provided as an alphabetic string of size 2 only.")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("guayaqui","ec"))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] Error of extenal API arguments: city=guayaqui country=ec")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("guayaquil","e"))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] country argument should be provided as an alphabetic string of size 2 only.")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("guayaquil",""))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] country argument should be provided as an alphabetic string of size 2 only.")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("","e"))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] city argument should be provided as an alphabetic string only.")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("","ec"))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] city argument should be provided as an alphabetic string only.")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("gu1ayaqui","ec"))
        self.assertEqual(request.status_code, 404)
        self.assertEqual(request.json()["message"], "[Error] city argument should be provided as an alphabetic string only.")

        request = requests.get(os.environ.get("GLOBANT_API_URL_FORMAT").format("guayaquil","ec"))
        self.assertEqual(request.status_code, 200)

        
        data =  {     'coord': {'lon': -79.9, 'lat': -2.1667}
                    , 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}]
                    , 'base': 'stations'
                    , 'main': {'temp': 297.13, 'feels_like': 297.75, 'temp_min': 297.13, 'temp_max': 297.56, 'pressure': 1011, 'humidity': 83}
                    , 'visibility': 10000
                    , 'wind': {'speed': 5.14, 'deg': 220}
                    , 'clouds': {'all': 75}
                    , 'dt': 1652157264
                    , 'sys': {'type': 1, 'id': 8534, 'country': 'EC', 'sunrise': 1652094917, 'sunset': 1652138209}
                    , 'timezone': -18000
                    , 'id': 3657509
                    , 'name': 'Guayaquil'
                    , 'cod': 200}
        validator = formatValidator()
        readable_data = validator.format_response(data)
        self.assertEqual(readable_data["location_name"], 'Guayaquil, EC')
        self.assertEqual(readable_data["temperature"],"24.13 °C or 75.43 °F")
        self.assertEqual(readable_data["wind"],"Gentle breeze, 5.14 m/s, southwest")
        self.assertEqual(readable_data["cloudiness"],"high cloudy")
        self.assertEqual(readable_data["pressure"],"1011 hpa")
        self.assertEqual(readable_data["humidity"],"83%")
        self.assertNotEqual(readable_data["humidity"],"83")
        self.assertNotEqual(readable_data["humidity"],83)
        self.assertEqual(readable_data["sunrise"],"06:15")
        self.assertNotEqual(readable_data["sunset"],"06:14")
        self.assertEqual(readable_data["sunset"],"18:16")
        self.assertNotEqual(readable_data["sunset"],"18:1")
        self.assertNotEqual(readable_data["sunset"],"180:15")
        self.assertEqual(readable_data["geo_coordinates"],"[-2.1667, -79.9]")
        self.assertEqual(readable_data["requested_time"],"2022-05-09 23:34:24")


        self.assertEqual(convert_unix_to_hour_minute(165215726400000),"00:00")
        self.assertEqual(convert_unix_to_time(165215726400000),"0000-00-00 00:00:00")
        self.assertEqual(is_between(31.50,32,50.24),True)
        self.assertEqual(is_between(31.50,31.50,50.24),True)
        self.assertEqual(is_between(31.50,80,50.24),False)

        self.assertEqual(get_wind_speed_description(62),"Hard Hurricane")
        self.assertEqual(get_wind_speed_description(15),"Moderate gale")

        self.assertEqual(get_cardinal_name("N"),"north")
        self.assertEqual(get_cardinal_name("W"),"west")
        self.assertEqual(get_cardinal_name("S"),"south")
        self.assertEqual(get_cardinal_name("E"),"east")


        self.assertEqual(get_cardinal_description(15),"north-northeast")
        self.assertEqual(get_cardinal_description(362),"wrong degrees adquired.")

        self.assertEqual(get_cloudiness_name(0),"no clouds")
        self.assertEqual(get_cloudiness_name(101),"no range covered")


if __name__ == '__main__':
    unittest.main()