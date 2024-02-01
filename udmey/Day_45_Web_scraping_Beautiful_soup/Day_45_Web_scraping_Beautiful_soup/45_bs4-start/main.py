# installed bs4 first using pip install bs4
from bs4 import BeautifulSoup


#####
## NOTE was getting error while open file
#return codecs.charmap_decode(input,self.errors,decoding_table)[0]
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 281: character maps to <undefined>

## Added encoding="utf8" to make it work NOt part of course slide
## but serched it online for error in code and added encoding="utf8" while
## opening website.html

##UTF-8 is one of the most commonly used encodings,
##and Python often defaults to using it.
##UTF stands for “Unicode Transformation Format”, and the '8' means
##that 8-bit values are used in the encoding. ...
##UTF-8 uses the following rules: If the code point is < 128,
##it's represented by the corresponding byte value.
#####

with open("website.html", encoding="utf8") as file:
    content = file.read()

##html.parser tells BS that its html file and we need to parse it    
soup = BeautifulSoup(content, "html.parser")
print(soup.title)           #output <title>Angela's Personal Site</title>
print(soup.title.name)      #output is "title" i.e name of tag
print(soup.title.string)    #output "Angela's Personal Site" i.e. without title Tag
print(soup)                 #output This will give complete HTML script in website.html
print(soup.prettify())      #output : this basically indents the HTML script
                            #        see the differen b/w soup and soup.prettify
                            #        prettify basically makes it look pretty

print(soup.a)               # <a> anchor tag


#IF we want all of the anchor tags and all of the paragraphs instead of not
#soup.title (title) or soup.a (anchor)
#then we need to use FIND_ALL() funciton with parameters what type of all tags we want

print("Anchor tags")
all_anchor_tags=soup.find_all(name="a")
print(all_anchor_tags)

print("paragraph tags")
all_paragraph_tags=soup.find_all(name="p")
print(all_paragraph_tags)

#IF we want just text part of any tag for example Paragraph excluding tags
all_paragraph_tags=soup.find_all(name="p")
print(all_paragraph_tags)

for tags in all_paragraph_tags:
     print(tags.getText())

# A way to get url's from all Anchor tags
for tags in all_anchor_tags:
     print(tags.get("href"))

# WE can have specific h1 tag value as well we can use id for it
heading=soup.find(name="h1",id ="name")
print(heading.string)  # .string give the value of h1 tag we need

#Similarly we cna do for h3 tag
#NOTE Class is reserved word in python which will give error
#when we use it in below. Thus we write class with underscore i.e class_
section_heading=soup.find(name="h3",class_="heading")
print(section_heading.string)  # .string give the value of h1 tag we need

# what we did below is , when we want particular paragrahp(p) with a (anchor)
# tag then use below selector. if we want to find all then use Select
# select_one gives first selected item
company_url=soup.select_one(selector="p a")
print(company_url)

name=soup.select_one(selector="#name")
print(name.getText())

headings=soup.select(".heading")
print(headings)

