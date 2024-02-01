print("tuples store mutiple pieces of information, we cant change it as we can do with list")
print("coordinates are good candidate of tuples")
coordinates = (4,5)
print(coordinates[0]) # will print 4
print(coordinates[1]) # will print 5
coordinates = [(4,5),(6,7),(8,9)]
print(coordinates[0]) # will print 4,5
print(coordinates[1]) # will print 6,7
print(coordinates[2]) # will print 8,9


print(coordinates[0][0]) # will print  4 from (4,5)
print(coordinates[0][1]) # will print  5 from (4,5)
