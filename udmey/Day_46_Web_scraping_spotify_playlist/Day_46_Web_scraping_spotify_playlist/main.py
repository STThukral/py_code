#https://www.billboard.com/charts/hot-100/
#For 2000-08-12
#https://www.billboard.com/charts/hot-100/2000-08-12/

import requests
from bs4 import BeautifulSoup


travel_year= input("Which year do you want to travel to (YYYY-MM-DD) : ")
#print(travel_year)
URL="https://www.billboard.com/charts/hot-100/"
DATE_URL=f'{URL}{travel_year}/'
#print(DATE_URL)


response=requests.get(DATE_URL)
#print(response) # This gives the code 200 if 400 then page not found
#print(response.text)
Best_100_BB_music=response.text
#print(Best_100_BB_music)


soup = BeautifulSoup(Best_100_BB_music,"html.parser")
print(soup.title) # gives the title of website in google Tab <title>Billboard Hot 100 – Billboard</title>
#print(soup.text) 

#For one movie to initally check we are going in right direction
#movie_number=soup.select("h3 a")
#song_name=soup.find(name="h3")  # using h3
#print(song_name.text)

#Create List
song_list=[]
song_names=soup.select("li ul li h3")

# while getting song title names it's coming with \n and \ts
#'\n\n\t\n\t\n\t\t\n\t\t\t\t\tSongwriter(s):\t\t\n\t\n'
# so added replace to make the list neat and clean
for songs in song_names:
    #song_list.append(songs.getText())
     song_list.append(songs.getText().replace('\n','').replace('\t',''))

print(song_list)

with open("Best_100_BB_music.txt",mode="w", encoding="utf-8") as fp:
    for songs in song_list:
            fp.write(f"{songs}\n")

print("Done !! File Created")
  




#Angela code
#from bs4 import BeautifulSoup
#import requests

#date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

#soup = BeautifulSoup(response.text, 'html.parser')
#song_names_spans = soup.select("li ul li h3")
#song_names = [song.getText().strip() for song in song_names_spans]

