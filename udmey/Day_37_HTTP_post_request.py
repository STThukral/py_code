# To Learn Advance Authentication and POST/PUT/DELETE request
#Day37 is it create Habit tracker

# will be created using Pixela (japenese API)
#https://pixe.la/

# Any habit like cycling, walking oe swimming etc
# we are making HTTP requestes to get data using , So using GET
#response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?q=London,UK",params=parameters)

#requests.get()
#requests.post()
#requests.put()
#requests.delete()

# In GET , we ask the external system to give us data using API
# and external syetem provides it in response

# In POST, we give external table piece of data and dont want response
# Like we want to post the data in google data, like twitter tweet
#then program will post the tweet using POST.

#PUT, wher eis update piece of data in the external service, update values in spreadsheet

#DELETE, when we want to delete the piece of information in external data.
#example if we want to delete tweet

#https://pixe.la/ gives steps to create user ,graph defination,
# get graph and post value to the graph

# used datetime.now() to get todays date and time and datetime.strftime() to format date

import requests
from datetime import datetime

USERNAME = "st1234st"
TOKEN = "abcd1234abcd1234abcd"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

#NOTE that user_params is like dictionary key and values
user_params = {
    "token":"abcd1234abcd1234abcd",
    "username":"st1234st",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


#Step 1 :- creating user account in pixela
#response =requests.post(url=pixela_endpoint,json=user_params)
# there is no need to response.json as we are not doing anything with information
#just checking output
#print(response.text)

#output below
#{"message":"Success. Let's visit https://pixe.la/@st1234st , it is your profile page!","isSuccess":true}


#Step2 :- create new graph in Pixela

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name":"Walking graph",
    "unit": "km",
    "type": "float",
    "color" :"shibafu"
    }

# request needs seperate token and thta is part of header so created
#seperate dicitonary for it
headers = {
    "X-USER-TOKEN":TOKEN
    }

# As graph is created so need to call it again , thus commneted
#response= requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

#output :- {"message":"Success.","isSuccess":true}
# Step 3 :- test graph
# now we can find graph using below url
# pixe.la/v1/users/st1234st/graphs/graph1.html (and it works , can see shibafu (which means green) )


#Step 4: - add pixels to the data (i.e. POSTing value to graph)

graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Got todays date and fomatted it into YYYYMMDD and given as input in graph_value dicitonary
# as date 
today = datetime.now()
# to crate pixels for days before today , we can use like
#today = datetime(year=2023,month=6,day=15)
#print(today)
formated_date = datetime.strftime(today, "%Y%m%d")
#print(formated_date)
graph_value = {
    "date": formated_date,
    #"quantity":"11.5"
    "quantity":input("How many Kilometers did you cycle today ? : ")
    }

#headers value will remain same

# As we posted it already so commenting below lines
response= requests.post(url=graph_value_endpoint,json=graph_value,headers=headers)
print(response.text)

#output {"message":"Success.","isSuccess":true}

#and now refresh https://pixe.la/v1/users/st1234st/graphs/graph1.html
#you will see pixel in light green 20230617


## NOW UPdate the pixels PUT AND DELETE
#Lets update pixels for today as its specified quantity as 11.5 we will make 10.9
#endpoint url has date as well
graph_update_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formated_date}"
put_value = {
    "quantity":"10.9"
    }
#response= requests.put(url=graph_update_value_endpoint,json=put_value,headers=headers)
#print(response.text)


## TO DELETE the day pixel we dont want any more
## commented is for the time beiing but works fine
graph_delete_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formated_date}"

#response= requests.delete(url=graph_delete_value_endpoint,headers=headers)
#print(response.text)
#output {"message":"Success.","isSuccess":true}

# output {"message":"Success.","isSuccess":true}
# data for today i.e. 20231806 should be deleted 
