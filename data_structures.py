lort ={"name": "The Fellowship of the Ring","author": "JRR Tolkien", "year": 1954, "genre": "adventure"}

print(lort["author"])
print("The first book of Lord of the rings is", lort["name"], ", published on", lort["year"])

lort["name"] = "The Two Towers"

print("The second book of Lord of the rings is", lort["name"], ", and it was also published on", lort["year"])

lort["name"] = "Return of the King"
lort["year"] = 1955
lort["movie"] = 2003

print("The last book of Lord of the rings is", lort["name"], ", published on", lort["year"], "with a movie was released in", lort["movie"])

del lort["genre"]

print(lort)

movies = {'blade runner', 'poor things', 'the godfather', 'apocalypse now', 'snatch'}
movies.add('fear and loathing in las vegas')

watchlist = {'poor things', 'anatomy of a fall', 'dune', 'oppenheimer', 'snatch'}

print(movies & watchlist)
