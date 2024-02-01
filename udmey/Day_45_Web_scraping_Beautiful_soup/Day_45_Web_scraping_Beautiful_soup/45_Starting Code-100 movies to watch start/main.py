import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
#print(response) # This gives the code 200 if 400 then page not found
#print(response.text)
Best_100_movies_online = response.text

soup = BeautifulSoup(Best_100_movies_online,"html.parser")
print(soup.title) # gives the title of website in google Tab
#print(soup.text)

#For one movie to initally check we are going in right direction
#movie_title=soup.find(name="h3")
#print(movie_title.text)


movie_title=soup.find_all(name="h3")
#print(movie_title.text)

# Create list
movie_list=[]
reversed_movie_list=[]
for m_title in movie_title:
    #print(m_title.text)
    movie_list.append(m_title.text)
#
# Reverse the order of movie list
#
#e.g. 100) Stand By Me moved to last as it is first in list in website
#   and 1) The Godfather moved to start of list as it was at then end of list 
movie_list.reverse()
print(movie_list)

## Writing list into file
## in tutorial not sure encoding="utf-8" was missing which i added to make it work in code
with  open("Best_100_movie_list_file.txt",mode="w", encoding="utf-8") as fp:
        for movie in movie_list:
            fp.write(f"{movie}\n")
            
        print("Done !! . File Created")
    


