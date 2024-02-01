print("this is first script")
print("but not the last script")
print("there once was a man named Sharad")
print("he was 35 year old")

print("he liked his name Sharad")
print("but didn't like being 35")

print("")
character_name = "Sharad"
character_age = "35"
print("change name and age into varaibles")
print("there once was a man named " + character_name)
print("he was " + character_age + " year old")

print("he liked his name " + character_name)
print("but didn't like being " + character_age)

print("")
print("printing Age as integer")
character_name = "Dave"
character_age = int(40)
print("he liked his name " + character_name)
print("but didn't like being " + str(character_age))

# Do below on IDLE to see type of character_age variable type
#type(character_age)
#<class 'int'>


print("")
print("upper and lowercase USE variable dot predefined function")
phrase = "Royal Academy"
print("This is " + phrase + " it's cool")
print("This is " + phrase.upper())
print("This is " + phrase.lower())

print("")
print("for TRUE/FALSE USE variable dot predefined function")
print(phrase.isupper()) # to check TRUE or FALSE dont include with string
print("")
print("using function one after another")
print(phrase.upper().isupper()) # this converted ISUPPER false to TRUE


print("")
print("length of string")
print(len(phrase))


print("")
print("in python index starts with 0")
print(phrase[0]) # first charatcer
print(phrase[3]) # fourth character

print("")
print("index function to get the position of character in string")
print(phrase.index("A")) # 6th poistion
print(phrase.index("Academy")) # 6th poistion
print(phrase.index("y")) # 2nd index and third place in string

print("")
print("replace function")
print(phrase.replace("Royal","COMMON"))



