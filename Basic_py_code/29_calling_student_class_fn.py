print("calling class function")
from student_class_fn_28 import student

student1 = student("oscar","accouting", 3.1)
student2 = student("Phyllis","Business", 3.8)

#will print False on_honor_roll check if gpa >= 3.5 then true elase false
print(student1.on_honor_roll()) # calling student class from class funciton on_honor_roll
#will print True on_honor_roll check if gpa >= 3.5 then true elase false
print(student2.on_honor_roll())
