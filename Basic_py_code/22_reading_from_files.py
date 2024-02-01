print("reading from file")
print("")

#r+ reading and writing
#w write in file
#a append
#r read
#NOTE :- for give path file use double back slash
emp_file = open("C:\\sharad\\reading_from_files_emp_22.txt", "r") #read file
print(emp_file.readable())  # to check file in read mode (reault in boolean)
print(emp_file.readline()) # prints first line
print(emp_file.readline()) # prints second line

print("")
print("instead of printing line one by one as above , print all in loop")
for i in emp_file.readlines():  #remember its readline with "s" otherwise output will be different
    print(i)
emp_file.close() # close file
