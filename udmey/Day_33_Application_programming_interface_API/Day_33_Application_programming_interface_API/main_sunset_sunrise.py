import requests
from datetime import datetime

MY_LAT  = 52.435930
MY_LONG = -2.086180

def is_iss_overhead():
    response =requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data=response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude  = float(data["iss_position"]["latitude"])

    # creating tuple iss_position and storing longitude and latitude
    iss_position =(iss_longitude,iss_latitude)
    print(iss_position)
    if MY_LAT -5 <= iss_latitude <= MY_LAT+5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5:
        return True

def is_night():
    ## use https://www.latlong.net/ to get latitude and longitude
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0  # to get the time in 24 hour format
        }
    print(parameters["lat"])
    print(parameters["lng"])
  
    # to get data from end point
    #i.e. http://api.open-notify.org/iss-now.json
    response =requests.get(url="http://api.sunrise-sunset.org/json",params=parameters)
    #print(response)
    response.raise_for_status()
    data=response.json()
    print(data)

    # to split the string
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now()
    print(time_now)

    if time_now >= sunset or time_now <= sunrise:
        #its dark
        return True
        
#print(sunrise.split("T"))
#print(sunrise.split("T")[1].split(":")[0])
#print(sunset.split("T"))
#print(f' sunrise hour {sunrise}')
#print(f' sunset hour {sunset}')

#time_now = datetime.now()
#print(time_now)

#print(time_now.hour)

#print(f' current time hour {time_now.hour}')

# in 100 days we are sending email using day_32 lesson
#with while loop so that it can keep on checking
#import time
#while True:
#    time.sleep(60)
if is_iss_overhead() and is_night():
    print ("ISS overhead")
else:
    print(" wait for it come overhead")
