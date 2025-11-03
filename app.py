import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
"""
#File 1
for index, item in enumerate(data):
    print (f"{index}:{item["title"]}")

#File 2
x= int(input("Year After: "))
for index, item in enumerate(data):
    if  item["year"] > x :
        print (f"{index}:{item["title"]}, {item["year"]}")

#File 3
x= int(input("Year After: "))
for index, item in enumerate(data):
    if  item["year"] > x :
        print (f"{index}:{item["title"]}, {item["year"]}")


y= int(input("Year Before: "))
for index, item in enumerate(data):
    if  item["year"] < y :
        print (f"{index}:{item["title"]}, {item["year"]}")

#File 4
z= int(input("Year made in: "))
for index, item in enumerate(data):
    if  item["year"] == z :
        print (f"{index}:{item["title"]}, {item["year"]}")


#File 5
a= input("Movie name: ")
for index, item in enumerate(data):
    if  item["title"] == a :
        print (f"{index}:{item["title"]}")
"""
#File 6
b= input("Genres: ")
for index, item in enumerate(data):
    #print (f"{index}:{item["genres"]}")
    if  b in item["genres"]:
        print (f"{index}:{item["title"]}:{item["genres"]}")
            