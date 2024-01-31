#pass is one we do nothing , just pass
class User:
    pass  

# to intialize class use brackets
#user1 is called object , which we need to declare to use class
user1 = User()
print(user1)
# this is will give some thing <__main__.User object at 0x000001A0D0AF6D70>

#attribute for class defined as id and username is atatched to object user1
user1.id ="002"
user1.username ="sharad"

print(user1.id)
print(user1.username)

#constructor
#def __init__(self)


#init function will be called everytime we call class in obejcts
class users:
    def __init__(self):
        print(" new user is being created")

user1= users()
print(user1)

#attributes given in class
class user_info:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.followers =0       # called defualt value

user1= user_info(1234,"sharad")
print(user1.id)
print(user1.name)
print(user1.followers)        # this will be printed as 0 as vlaue not in paramter but by default in class as 0


#attributes are the things which class has
#methods are the things which class does

#attributes given in class
class user_info:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0       # called defualt value
        self.following = 0

    # method has self as first parameter  
    def follow(self,user):
        user.followers +=1
        self.following +=1


user1= user_info(1234,"sharad")
print(user1.id)
print(user1.name)
print(user1.followers)        # this will be printed as 0 as vlaue not in paramter but by default in class as 0

user2=user_info(4567,"Thukral")
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
