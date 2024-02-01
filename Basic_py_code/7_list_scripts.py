friends = ["friend1","friend2","friend3","friend4","friend5"]

print(friends)   # full list
print(friends[0]) # first value in list
print(friends[4]) # fifth value in list i.e. 4th value in array as array starts form 0

print("print value from back of list")
print(friends[-2])  # i.e 2nd value from back

print("print all values in list after first one")
print(friends[1:])
print("print all values in list after third one")
print(friends[3:])
print(friends[1:3]) # so 2nd and 3rd friend

print("MOdify position in  LIST")
friends[1] = "friend8"
print(friends[1])
print(friends)
 
