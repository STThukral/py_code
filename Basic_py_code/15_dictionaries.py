print("dictrionaries to store key value pair")
print("jan is key and January is Value and so on")
monthconversion = {
    "Jan" : "january",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "april",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"

}

print("")
print(monthconversion["Mar"])
print(monthconversion["Aug"])
print(monthconversion.get("Dec"))  # another way
# to get default value is key doesn't exists in dictitonary
print(monthconversion.get("MINE"))  # min is not key so result will show NONE
# we can give user defined error msg
print(monthconversion.get("MINE","Dave said MINE is not in dictionary")) #will give message as output
print(monthconversion.get("Dec","Dave said MINE is not in dictionary"))  # will give value of Dec as its in dicitonatry
