#try:         something that might cause exception
#except:      Do this if there WAS AN exception
#else:        Do this if there were NO excpetions     
#finally:     Do this no matter what happens
#error_message get hold of error message
#raise : raise our own exception in any case 


#try:
#    file = open("a_file.txt")
#except:
#    print("File not found")
    # as file doesnt exists then create a file in exception
    # so process should not stop
#    print("We will be creating file in except")
#    file = open("a_file.txt","w")    
#    file.write("writing something")
#    file.close()
    
# we can have multiple except for different statement in try
# in below example we are tyring to find b_file.txt , which doesnt exist
#process will go in except and create new file
#but if next statement in try gives error , it will still create file
#for example dictionary key deosnt exists so error should be thrown for it

try:
    file_b = open("b_file.txt")
    a_dict = {"key":"value"}
    #print(a_dict["not_a_key"])
    print(a_dict["key"])
except FileNotFoundError:
    print("File not found b")
    # as file doesnt exists then create a file in exception
    # so process should not stop
    print("We will be creating file in except b")
    file_b = open("b_file.txt","w")
    file_b.write("writing something")
except KeyError as error_message:
    # to see where or why we get error use error_message in except
    print(f" The key {error_message} doesnt exists")
else:
    # when we comment line print(a_dict["not_a_key"])
    # that means no error from try block and content of file will be printed
    content = file_b.read()
    print(content)
finally:
    file_b.close()
    print(" we closed the file in finally block")
    #forcing to raise any error
    #raise TypeError("This error i made up")   
