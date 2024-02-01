l_numbers = [4,8,815,16,23,42]
friends = ["friend1","friend2","friend3","friend4","friend5"]
print(friends)
friends.append("MIKE")  #add mike at the end of list
print(friends)
friends.insert(1,"TOM") # add TOM at 2nd position as array starts from 0
print(friends)
friends.remove("friend2") #removing sprcific item vlue from list
print(friends)
friends.pop()  #poped MIKE from the list (last one removed)
print(friends)
print(friends.index("TOM")) #find position of TOM in list
print(friends.count("friend5"))  # count the howm many times "friend5" in list
print(friends.sort()) #all starts with "f"
print("")
print("before sorting")
print(l_numbers)
print("after sorting")
l_numbers.sort()       # sort lsit items 
print(l_numbers)
print("Reverse LIST")
l_numbers.reverse() #reverse list items
print(l_numbers)

print("")
print("copy list friends to friends2")
friends2 = friends.copy() # copy list 
print(friends2)
