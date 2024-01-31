#API Authentication
#Authenticate our self with API provider, so that we can access more data
#API which requires , before that in previous chapters it was all free
#Weather data is valuable and will be chargable as well i.e. not free
#to prevent people from abusing data is providing API key , providing username
#and password

#When using new API we should read the document
#created account in https://home.openweathermap.org/
#username is stpython2023@gmail.com
# goto "API Keys" and grab key from "create key" and give name to the key
# i given name as "python"
# if we use URL wihtout API key we will get error as below :-
#{"cod": 401,"message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}

#api_key = "bc249d70f7eae20867c28cfe95b726bb"

#to check API KEY works or not 
#https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=bc249d70f7eae20867c28cfe95b726bb
#We will get output as below :-

#{"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}]
# ,"base":"stations","main":{"temp":302.45,"feels_like":302.16,"temp_min":300.68,"temp_max":304.26,"pressure":1012,"humidity":41}
# ,"visibility":10000,"wind":{"speed":7.72,"deg":90},"clouds":{"all":12},"dt":1686407422,
# "sys":{"type":2,"id":268730,"country":"GB","sunrise":1686368646,"sunset":1686428152},"timezone":3600,
# "id":2643743,"name":"London","cod":200}
#https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&appid=bc249d70f7eae20867c28cfe95b726bb
#https://api.openweathermap.org/data/2.5/onecall?lat=51.5085&lon=-0.1257&appid=bc249d70f7eae20867c28cfe95b726bb

import requests
api_key = "bc249d70f7eae20867c28cfe95b726bb"

parameters = {
        "appid": api_key,
        #"lat":51.5085,
        #"lon":-0.1257,
        
        }

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?q=London,UK",params=parameters)
#response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status() # rasie an exception if any
print(response.json())
weather_data=response.json()
london_longitude=(weather_data["coord"]["lon"])
london_latitude=(weather_data["coord"]["lat"])
print (f'london_longitude : {london_longitude}')
print (f'london_latitude : {london_latitude}')

Clouds_condition=(weather_data["weather"][0]) # complete list
print(f'Clouds_condition : {Clouds_condition}')
#After getting dicitonary from list get id for cloud weather
Clouds_description=(weather_data["weather"][0]["description"])
Clouds_condition=(weather_data["weather"][0]["id"])
print(f'Clouds_description : {Clouds_description}')
print(f'Clouds_condition : {Clouds_condition}')
if Clouds_condition < 801:
    print("Bring your brolli, it may rain")
else:
    print("only few cloudy")

temperature =(weather_data["main"])
print(f'temperature : {temperature}')
#kelvin to degree
#temp in kelivn - standard number = temprature in degree
#304.29K − 273.15 = 31.14°C
temp = (weather_data["main"]["temp"])
temp_feels_like = (weather_data["main"]["feels_like"])
temp_min = (weather_data["main"]["temp_min"])
temp_max = (weather_data["main"]["temp_max"])

temp = round(temp - 273.15,1)
temp_feels_like = round(temp_feels_like - 273.15,1)
temp_min = round(temp_min - 273.15,1)
temp_max = round(temp_max - 273.15,1)

print(f'temp : {temp}')             
print(f'temp_feels_like : {temp_feels_like}')             
print(f'temp_min : {temp_min}')             
print(f'temp_max : {temp_max}')             


# Environment variables
# for convenience ( not need to chnage them or write them again n again)
# for security
# storing api key in environment variable and calling in code
# api_key = os.environ.get("OWM_API_KEY")
