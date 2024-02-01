

class user:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

# function will accept the fucntion but we need pass if we need to pass
# the argument then we need to use
#  args and kawrgs (unlimited position argument in *args
    #               and unlimited keyword arguments in **kwargs)
def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):  # functions inputs and args[0] is first positional
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper    

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user= user("sharad")
new_user.is_logged_in = True # if its true then we will get create_blog_post executed 
create_blog_post(new_user)


