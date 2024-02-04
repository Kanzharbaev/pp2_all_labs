movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def high_imdb(movie):
    for i in movies:
        if i["name"]==movie:
            return i["imdb"]>5.5

print(high_imdb("We Two"))
#Write a function that returns a sublist of movies with an IMDB score above 5.5.

def high_imdb_movie():
    returns=[]
    for i in movies:
        if i["imdb"]>5.5:
            returns.append(i["name"])
    return returns
print(high_imdb_movie())
#Write a function that takes a category name and returns just those movies under that category.
def category(category_name):
    a=[]
    for i in movies:
        if i["category"]==category_name:
            a.append(i["name"])
    return a

print(category("Romance"))
#Write a function that takes a list of movies and computes the average IMDB score.
def avg():
    summa=0
    cnt=0
    for i in movies:
        cnt+=1
        summa+=i["imdb"]
    return summa/cnt

print(avg())
#Write a function that takes a category and computes the average IMDB score.
def avg_for_category(category):
    cnt=0
    summa=0
    for i in movies:
        if i["category"]==category:
            cnt+=1
            summa+=i["imdb"]
    return summa/cnt

print(avg_for_category("Comedy"))
