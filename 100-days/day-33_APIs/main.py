import requests 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # <Response [200]>
print(response.status_code) # 200>

data = response.json()
print(data)
    # {
    # 'iss_position': {
    #     'longitude': '-22.4540', 
    #     'latitude': '48.6545'
    #     }, 
    # 'timestamp': 1675618164, 
    # 'message': 'success'
    # }

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(longitude, latitude)