import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
#for index, item in enumerate(data):
   # print (f"{index}:{item["title"]}")

#x= int(input("Year After: "))
#print(x)

for index, item in enumerate(data):
    if {index}:{item["year"]} > x:
        print (f"{index}:{item["title"]}")
        
    