print("This is eample where ChineseChef cook all the thing which chef_30 can do")
print("Along with do extra cook, so this means inheriting all the skills from")
print("from script chef_30 and adding extra skills what chinese chef can do")

#so instead of writing all the functions in chef_30 code, just inherit it
# link with chef_30 script
from chef_30 import chef

class ChineseChef(chef):
    def make_special_dish(self):
        print("The chef makes ORANGE CHICKEN") # This is something we are inherting Chef_30 and then overwriting it with own staement
    def make_fried_rice(self):
        print("The chef makes fried rice")

    
