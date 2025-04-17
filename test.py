from person import Person
from network import MovieNetwork

# Creating people
jerry = Person("Jerry")
bright = Person("Bright")
isaac = Person("Isaac")
patience = Person("Patience")

# Adding movies
jerry.add_movies(["Avengers", "Loki", "G.O.T"])
bright.add_movies(["The Witcher", "Loki", "Lupin"])
isaac.add_movies(["Titanic", "Red", "G.O.T"])
patience.add_movies(["Avengers", "Loki", "Power"])

# Add friends
jerry.add_friend(bright)
jerry.add_friend(isaac)
isaac.add_friend(patience)

# Building network
network = MovieNetwork()
for person in [jerry, bright, isaac, patience]:
    network.add_person(person)

print(network.get_most_popular_movie("Jerry"))