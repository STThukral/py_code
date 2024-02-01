# Web Scraping will be done on website https://news.ycombinator.com/
# example of restriction on scrapping data
# for example if we take linkedin URL and type robots.txt then it will give
#us list of things we cant do to site
#https://www.linkedin.com/robots.txt
#that's lot of sites use reCAPTCHA to see if its human who is accessing there
#site or its a robot (means some code trying to do web-scraping)

## So do WEB-SCRAPING with ETHICS

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
#print(response)
#output <Response [200]> menas all good if this would have been 400 then issue
#print(response.text) # give html page code for website
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
print(soup.title) # Shows the Title from Tab

#Code to find one
#article_tag=soup.find(name="a", rel="noreferrer") # in tutorial its class here its ref as per html source code we used ref
#print(article_tag.getText())  # to get title we used getText
# output "Kevin Mitnick has died"
#article_link=article_tag.get("href")
#print(article_link)

#score_tag=soup.find(name="span", class_="score")
#print(score_tag)
#article_upvote=score_tag.getText()
#print(article_upvote)


# Code to find ALL
#Defining List
article_texts=[]
article_links=[]
article_scores=[]
article_tags=soup.find_all(name="a", rel="noreferrer") # in tutorial its class here its ref as per html source code we used ref

for titles in article_tags:
    #print(titles.getText())  # to get title we used getText
    #print(titles.get("href"))
    #Appending List
    article_texts.append(titles.getText())
    article_links.append(titles.get("href"))


score_tags=soup.find_all(name="span", class_="score")

for scores in score_tags:
   # print(scores.getText())
    #Appending List
   #spliting scores and getting integer value of scores
     article_scores.append(int(scores.getText().split()[0]))

print(article_texts)
print(article_links)
print(article_scores)
#print(max(article_scores))
print(article_scores.index(max(article_scores))) # to get index value of Maximum score

# max(article_scores) gives max value in list
# article_scores.index(max(article_scores)) gives index value for Max value
Max_score_index_value=article_scores.index(max(article_scores))

print(article_scores[Max_score_index_value])
print(article_texts[Max_score_index_value])
print(article_links[Max_score_index_value])      

#output
#2745
#Kevin Mitnick has died
#https://www.dignitymemorial.com/obituaries/las-vegas-nv/kevin-mitnick-11371668


#print(article_scores[0].split()[0]) # to split it into 2 seperate entities in list and then select first one
