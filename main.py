import requests
from twilio.rest import Client
import os


API_KEY = os.environ.get("OWM_API_KEY")
LAT = os.environ.get("LAT")
LON = os.environ.get("LON")
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("ACCOUNT_SID")

auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat":LAT,
    "lon":LON,
    "appid":API_KEY,
    "cnt":4
}
response = requests.get(url=API_ENDPOINT,params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)

will_rain = [True for i in range(len(data["list"])) if data["list"][i]["weather"][0]["id"] < 700]
print(will_rain)
if True in will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Today is going to rain. Remember to bring an umbrella☔.",
        from_=os.environ.get("FROM"),
        to=os.environ.get("TO"),
    )

    print(message.status)


