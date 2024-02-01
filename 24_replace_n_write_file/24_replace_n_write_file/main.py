
#with open("invited_names.txt") as names:
#    contents = names.read()
    #print(contents)
#names= open("invited_names.txt")
#for contents in names.readlines():
#    letter_file = open("starting_letter.txt","r")
#    for i in letter_file.readlines():
#        x=i.replace("[name]",contents)
#        file_name = print(f' letter_to_{contents}.txt')
#        invite_letter= open("C:\\sharad\\panda_scripts\\udemy\\24_replace_n_write_file\\send_files\\file_name","w")
#        invite_letter.write(x) 

PLACEHOLDER="[name]"    
with open ("./invited_names.txt") as names_file:
    names=names_file.readlines() # readlines will chnage invidiual names in list
    print(names)

with open("./starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        striped_name =name.strip()
        #print(name)
        print(striped_name)
        new_letter= letter_contents.replace(PLACEHOLDER,striped_name)
        #print(new_letter)
        with open(f"./send_files/letter_for_{striped_name}.txt","w") as sending_letter:
            sending_letter.write(new_letter)
