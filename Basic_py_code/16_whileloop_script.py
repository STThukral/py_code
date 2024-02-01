print("while loop")

i = 1
while i <= 5:
    print(" This is number : " + str(i))
    i += 1

print(" while loop ends")    

print("")

print("for loop")
for i in range(5):  # this will print 0 to 4
    print("This is number : " + str(i))
print("for loop ends")    

print("")
print("for loop")
for i in range(1,5):  # this will print 1 to 4
    print("This is number : " + str(i))
print("for loop ends")    


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
