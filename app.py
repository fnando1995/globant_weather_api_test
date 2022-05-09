from flask import Flask, Response, request
import json
from libraries.weather import *
app = Flask(__name__)
@app.route("/weather")   
def weather():
    response_data = dict()
    status_code   = 404         # 200 ok | 404 not ok

    city          = request.args.get("city")
    country       = request.args.get("country")

    if city is None or not city.isalpha() :
        response_data["message"] = "[Error] city argument should be provided as an alphabetic string only."
        status_code = 404
    elif country is None or not country.isalpha() or len(country)!=2:
        response_data["message"] = "[Error] country argument should be provided as an alphabetic string of size 2 only."
        status_code = 404
    else:
        weather = Weather()
        response_data["message"],status_code =  weather.call_weather(city,country) 
    return Response(json.dumps(response_data,ensure_ascii=False),
                    status=status_code,
                    mimetype="application/json")

if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_HOST"), port=int(os.environ.get("FLASK_PORT")))  #os.environ.get("PORT") #os.environ.get("FLASK_HOST")