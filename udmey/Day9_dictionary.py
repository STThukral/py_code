print("")
print("print dictionary and assign changed values to new dictionaries")
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

print("original Dictionary :", student_scores)

student_grades={}
grades=""
for key in student_scores:
    #print (student_scores[key])
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        grades = "Outsanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        grades = "Exceeds Excpectations"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        grades = "Exceeds Excpectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        grades = "Acceptable"
    elif student_scores[key] <= 70:
        grades = "Fail"
    student_grades[key] = grades

print("Changed to grades Dictionary :", student_grades)

print(" ")
print("Nested  Dicitonary in a Dictionary")
travel_log = {
    "France": ["paris","lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}

print(travel_log)

travel_log1 = {
    "France": {"cities_visited": ["paris","lille","Dijon"], "total_visits": 12},
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}

print(travel_log1)


print(" ")
print("Nested  Dicitonary in a list")

travel_log1 = [
    {"country":"France",
     "cities_visited": ["paris","lille","Dijon"],
     "total_visits": 12
    },
    {"country":"Germany",
     "cities_visited":["Berlin","Hamburg","Stuttgart"],
     "total_visits": 12
    }
]
print(travel_log1)




print(" ")
print(" Add nested dictonary on a list")
print("used function to add new dictionary to the list")

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name,visits,visit_cities):
    new_country={}
    new_country["country"] = country_name
    new_country["visits"]  = visits
    new_country["cities"]  = visit_cities
    
    travel_log.append(new_country) 
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


print(" ")
print(" code to ask for user entry and add into dictionary")
print(" while loop to keep on asking untill its asnwered as 'no")
print("print the max bid")
#from replit import clear
bid_dictonary={}
user_input = True
while user_input:
    user_name = input("Please enter your name :")
    bid_price = float(input("Please enter your bid price :"))

    bid_dictonary[user_name] = bid_price
    user_input = input ("Any other user want to bid 'yes/no' :")
    if user_input == 'no':
        user_input = False
    
print(bid_dictonary)
max_value =0
max_bid_name=""
for key in bid_dictonary:
    bid_value= bid_dictonary[key]
    if bid_value > max_value:
        max_value = bid_value
        max_bid_name = key
         
print(f'The winner is {max_bid_name} with a bid of {max_value}')     
                



