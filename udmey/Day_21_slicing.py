
piano_keys = ["a","b","c","d","e","f","g"]

#slicing from 2 to 5
print(piano_keys[2:5])
# output ['c', 'd', 'e']

#slicing from 2 uptill end
print(piano_keys[2:])
# output ['c', 'd', 'e', 'f', 'g']

#slicing uptill 5
print(piano_keys[:5])
# output ['a', 'b', 'c', 'd', 'e']


#slicing from 2 to 5 skip 2
print(piano_keys[2:5:2])
# output ['c', 'e']

#slicing first only
print(piano_keys[:1])
# output ['a']

#slicing and getting first two 
print(piano_keys[:2])
# output ['a', 'b']

#slicing from back and getting all other than last  
print(piano_keys[:-1])
# output ['a', 'b', 'c', 'd', 'e', 'f']


#reverse the list  
print(piano_keys[::-1])
# output ['g', 'f', 'e', 'd', 'c', 'b', 'a']


#same works for piano tuples
piano_tuples=("do","re","mi","fa","so","la","ti")

print(piano_tuples[2:5])

#output ('mi', 'fa', 'so')

