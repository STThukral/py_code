#https://opentdb.com/
#https://opentdb.com/api_config.php
#https://opentdb.com/api.php?amount=10&type=boolean

# to check the actual HTML value
#https://www.freeformatter.com/html-escape.html#before-output
# when we run below url and get question we get &quot;, &#039;etc
# to get the clear value without these codes we can check the actual string
#using above url
#he song &quot;Mystery Train&quot; was released by
#artist &quot;Little Junior&#039;s Blue Flames&quot; in 1953. (True/False): true
#output of baove line is:-
#he song "Mystery Train" was released by artist
#"Little Junior's Blue Flames" in 1953. (True/False): true


# we are doing below execrcise to get question form API instead of hardcode dictionary
#every time we get randon 10 questoin with answer as true/false

import requests

Q_BOOLEAN = "boolean"
parameters = {
        "amount": 10,
        "type": Q_BOOLEAN
        }
response = requests.get(url="https://opentdb.com/api.php/json",params=parameters)
response.raise_for_status() # rasie an exception if any
data=response.json()
#print(data["results"]) # as the data is prtinted as below response_code is 0
                           # i.e. data ran sucessfully and we need result to be
                           # in dictionary that's why we used (data["results"]) 
#===== RESTART: C:\sharad\panda_scripts\udemy\34_quizzler_app_start\data.py =====
#{'response_code': 0, 'results': [{'category': 'Entertainment: Video Games'
#                                  , 'type': 'boolean', 'difficulty': 'hard'
#                                  , 'question': 'In &quot;The Sims&quot; series
#                                  , the most members in a household you can have
#                                  is 8.', 'correct_answer': 'True',
#                                  'incorrect_answers': ['False']},


# And now assign it to question_data
question_data = data["results"]






# sample data in dictonary
#question_data = [
#    {
#        "category": "Science: Computers",
#        "type": "boolean",
#        "difficulty": "medium",
#        "question": "The HTML5 standard was published in 2014.",
#        "correct_answer": "True",
#        "incorrect_answers": [
#            "False"
#        ]
#    }
# ]
