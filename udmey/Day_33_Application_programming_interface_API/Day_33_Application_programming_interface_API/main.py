import requests

# to get data from end point
#i.e. http://api.open-notify.org/iss-now.json
response =requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# it will give output like <Response [200]>. it has meaning
# like normally when we some page not found we get 404 error
# 1XX : Hold on     (i.e something is in process)
# 2XX : Here you go  (i.e. data processed well)
# 3XX : go away       (i.e. dont have permission)
# 4XX : you screwed up (i.e yo are looking for something deosnt exists)
#e.g. chnage the http URL little bit (for e.g change "iss" to "is"
#and you will get below error
#<Response [404]>
#404
# can check sstaus code using url https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# or type "http status codes" in google

# to get status of above url
response.raise_for_status()
#get data in json format
data=response.json()
print(data)
# to narrow down to particular key we give it like
iss_pos=response.json()["iss_position"]
print(f' getting latitude and longitude {iss_pos}')
# or being specific
iss_pos_longi=response.json()["iss_position"]["longitude"]
print(iss_pos_longi)

longitude = data["iss_position"]["longitude"]
latitude  = data["iss_position"]["latitude"]

# creating tuple iss_position and storing longitude and latitude
iss_position =(longitude,latitude)
print(iss_position)
# and use it https://www.latlong.net/


