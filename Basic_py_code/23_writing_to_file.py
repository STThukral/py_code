print("Writing and appending Files")

emp_file = open("C:\\sharad\\reading_from_files_emp_22.txt", "a") #append file

emp_file.write("\nToby - Human Resources") #\n is to append line in file with ne line

emp_file.close()


#create new file
emp_file1 = open("C:\\sharad\\reading_from_files_emp_22_1.txt", "w") #write new file
emp_file1.write("\nToby - Human Resources") #\n is to write line in file with ne line

emp_file1.close()


# creating html file
emp_file1 = open("C:\\sharad\\reading_from_files_emp_22_1.html", "w") #write new file
emp_file1.write("<p>Toby - Human Resources This is HTML</p>") #\n is to write line in file with ne line

emp_file1.close()
