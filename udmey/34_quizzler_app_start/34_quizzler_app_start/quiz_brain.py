import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        #question we were getting from data.py we were having some codes
        #against double codes,single code etc . so used html unescape
        # to translate them to actual single or double code etc.
        #check eample in data.py
        q_text = html.unescape(self.current_question.text) 
        return f"Q.{self.question_number}: {q_text}" 
        #user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # commented so that instead displaying as message , we want color
            # display green as True  and false as Red
            #print("You got it right!")
            return True
        else:
            # commented so that instead displaying as message , we want color
            # display green as True  and false as Red
            #print("That's wrong.")
            return False

        # commented so that instead displaying as message , we want color
        # display green as True  and false as Red
        #print(f"Your current score is: {self.score}/{self.question_number}")
        #print("\n")
