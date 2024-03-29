from multipe_choice_26 import question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]    
    
questions = [
    question(question_prompts[0], "a"), #a,c,b are answers
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
       answer = input(question.prompt)
       if answer == question.answer:
               score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " Correct")
       
run_test(questions)
