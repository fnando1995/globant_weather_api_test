from libraries.utils import *

class formatValidator():        
    def __init__(self):
        self.response = None
        self.human_response = None
            
    def format_response(self,response):
        """
        method created to integrate all format validations
        """
        self.response=response
        self.human_response={}
        self.human_response["location_name"]=self.format_location_name()
        self.human_response["temperature"]=self.format_temperature()
        self.human_response["wind"]=self.format_wind()
        self.human_response["cloudiness"]=self.format_cloudiness_2()
        self.human_response["pressure"]=self.format_pressure()
        self.human_response["humidity"]=self.format_humidity()
        self.human_response["sunrise"],self.human_response["sunset"]=self.format_sunrise_sunset()
        self.human_response["geo_coordinates"] = self.format_geo_coordinates()
        self.human_response["requested_time"]=self.format_requested_time()
        return self.human_response

    def format_location_name(self):
        """
        method for validate the location name key for response
        """
        return self.response["name"] + ", " + self.response["sys"]["country"]

    def format_temperature(self):
        """
        method for validate the temperature key for response.
        returns celsius and fahrenheit degrees
        """        
        temp_kelvin = self.response["main"]["temp"]
        temp_celsius = round(temp_kelvin - 273,2)
        temp_fahrenheit = round((9/5*(temp_celsius)) + 32,2)
        return f'{temp_celsius} °C or {temp_fahrenheit} °F'

    def format_wind(self):
        """
        method for validate the wind description key for response
        return a description for the wind speed, the wind speed in 
        meters/seconds and the cardinal directions of the wind in a
        string.
        """
        speed = self.response["wind"]["speed"]
        degrees = self.response["wind"]["deg"]
        return f"{get_wind_speed_description(speed)}, {speed} m/s, {get_cardinal_description(degrees)}"

    def format_cloudiness(self):
        """
        method for validate the cloudiness key for response.
        this uses the field weather which could or could not
        have a reference for the clouds.
        """        
        data = self.response["weather"]
        clouds = [dictionary["description"] for dictionary in data if "Clouds" in dictionary.keys()]
        if len(clouds)==1:
            return clouds[0]
        else:
            return "no cloud information displayed"

    def format_cloudiness_2(self):
        """
        method for validate the cloudiness key for response
        this uses a created range defined by the OKTAS range
        for the clouds which uses a percentage of the cloud
        covering the sky.
        """        
        percentage = self.response["clouds"]["all"]
        return get_cloudiness_name(percentage)


    def format_pressure(self):
        """
        method for validate the pressure key for response
        """
        return f"{self.response['main']['pressure']} hpa"

    def format_humidity(self):
        """
        method for validate the humidity key for response
        """        
        return f"{self.response['main']['humidity']}%"

    def format_sunrise_sunset(self):
        """
        method for validate the sunrise and sunset keys for response
        this uses a unix to time (hour and minute) convertion
        for been human redable.
        """        
        sunrise =  int(self.response["sys"]["sunrise"])+int(self.response["timezone"])
        sunset  =  int(self.response["sys"]["sunset"])+int(self.response["timezone"])
        return convert_unix_to_hour_minute(sunrise),convert_unix_to_hour_minute(sunset)

    def format_geo_coordinates(self):
        """
        method for validate the geographical coordinates key for response
        """
        return str([self.response["coord"]["lat"],self.response["coord"]["lon"]])


    def format_requested_time(self):
        """
        method for validate the requested_time key for response
        """
        return convert_unix_to_time(int(self.response["dt"])+int(self.response["timezone"]))