import requests
import json

hovedsteder  = {
    "Oslo": {
        "latitude": 59.91,
        "longitude": 10.76
    },
    "Paris": {
        "latitude": 48.85,
        "longitude": 2.35
    },
    "London": {
        "latitude": 51.5,
        "longitude": -0.1
    }
}

hok = input("Vil du skrive egne hovedsteder, eller koordinater? ('h' eller 'k') > ")
while hok != "k" and hok != "h":
    hok = input("Vil du skrive egne hovedsteder, eller koordinater? ('h' eller 'k') > ")
if hok == "k":
    latitude = input("Latitude > ")
    longitude = input("Longitude > ")
else:
    land = input("Skriv en hovedstad. > ").title()
    while land not in hovedsteder.keys():
        land = input(f"{land} er ikke i listen. Skriv en hovedstad > ")
    latitude = hovedsteder[land]["latitude"]
    longitude = hovedsteder[land]["longitude"]
respons = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={latitude}&lon={longitude}" , headers={ 'User-Agent': 'Python'})
data = respons.json()
with open("api.json", "w", encoding="utf-8") as fil:
    json.dump(data, fil, indent=2, ensure_ascii=False)

enheter = data["properties"]["meta"]["units"]
værtype = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
grader, vind = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"], data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]
if "wind_speed_of_gust" in data["properties"]["timeseries"][0]["data"]["instant"]["details"].keys():
    gust = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed_of_gust"]
else:
    gust = "?"

print(f"Det er {grader} grader {enheter['air_temperature']}. Det vil være {vind}({gust}) {enheter['wind_speed']} vind.")