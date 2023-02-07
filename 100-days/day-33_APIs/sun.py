import requests 
from datetime import datetime

MY_LAT = 51.590050
MY_LONG = -0.781600

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise) # 2023-02-06T07:31:49+00:00
# print(sunrise.split("T")) # ['2023-02-06', '07:31:49+00:00']
print(sunrise.split("T")[1].split(":")) # ['07', '31', '49+00', '00']
print(sunrise.split("T")[1].split(":")[0]) # 07

time_now = datetime.now()
print("25", time_now.hour)
# print(time_now) # 2023-02-06 15:50:35.923714

