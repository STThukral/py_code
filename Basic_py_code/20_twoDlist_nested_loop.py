print("2 dimensional list")

number_list = [       # list inside list
    [1 ,2 ,3],
    [4 ,5 ,6],
    [7 ,8 ,9],
    [0]
  ]

print(number_list[0])  # first list
print(number_list[0][1])  # second element in first list

print("")
print("for loop")
for row in number_list:
    print(row)


print("")
print("nested loop , printing every invidual number in list")
for row in number_list:
    for col in row:
        print(col)
