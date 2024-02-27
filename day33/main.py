from pandas.core.dtypes.dtypes import datetime
import requests 

SUNSET_SUNRISE_API = "https://api.sunrise-sunset.org/json"
ISS_API = "http://api.open-notify.org/iss-now.json"

MY_LAT = -11.892213
MY_LONG = 18.788367

def is_iss_overhead():
    response = requests.get(url=ISS_API)
    json = response.json()
    response.close()

    iss_lat = float(json["iss_position"]["latitude"])
    iss_long = float(json["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True
    return False

def is_night():
    params = {
        "lat": MY_LAT,
        "long": MY_LONG
    }
    request = requests.get(url=SUNSET_SUNRISE_API, params=params)
    json = request.json()
    request.close()
    results = json["results"]
    sunrise = int(results["sunrise"].split("T").split(":")[0])
    sunset = int(results["sunset"].split("T").split(":")[0])
    current_hour = datetime.now().hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    return False

if is_iss_overhead() and is_night():
    print("Ok")
