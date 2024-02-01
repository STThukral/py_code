from turtle import Turtle

ALIGNMENT ="Left"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f" Level : {self.score} ",align=ALIGNMENT,font=FONT)
        self.high_score =0
        
    def prev_high_score(self):
        #print("read from Files")
        score_file = open("C:\\sharad\\panda_scripts\\udemy\\23_turtle-crossing-start\High_score_file.txt", "r") #write file
        self.high_score = score_file.readline()
        self.write(f" Level : {self.score}  HIGH SCORE : {self.high_score}",align=ALIGNMENT,font=FONT)
        score_file.close() # to free resources
        
    def write_score_to_file(self):
        #print("Writing and appending Files")
        score_file = open("C:\\sharad\\panda_scripts\\udemy\\23_turtle-crossing-start\High_score_file.txt", "w") #write file
        score_file.write(f'{self.score}') #\n is to append line in file with ne line
        score_file.close()
        
    def increment_score(self):
        self.score += 1
        self.clear()
        self.goto(-280,260)
        self.write(f" Level : {self.score} ",align=ALIGNMENT,font=FONT)
        
    # below code is for reference
    # using with and as we dont need to expicitly
    # write score_file.close(), it will handle it implicitly
    # with open("file_name") as file:
    #        contents = file.read()
    #        print(contents)

    #Absolute file path
    # starts from root /work/project/talk.ppt
    #relative path
    #is where we currently are like in project folder and get the file name
    # ./talk.ppt
    # file path open(../../udmey) tells first 2 slashes are comman directory
    #and after that decide where to go we choose "udmey"
    

    
