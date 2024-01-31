from Day_17_quiz_data import question_data
from Day_17_quiz_brain import QuizBrain
class Question:
    def __init__ (self,q_text,q_answer):
        self.text = q_text
        self.answer = q_answer

# creating object "question1" and claaing class Question
#question1 = Question("Do you drink water","true")
#printing values in using object "question1" and attributes (text and answer)
#print(question1.text)
#print(question1.answer)

question_bank=[]    
for question in question_data:
    question_text = question["text"]
    question_answer =question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

#print(question_bank)
#print(question_bank[0].answer)

n_question= QuizBrain(question_bank)
    
while n_question.still_have_questions():    
    n_question.next_question()

print("You've completed the quiz")
print(f"your final score is : {n_question.score}/{n_question.question_number}")
