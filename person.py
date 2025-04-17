
class Person():
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.movies = []

    def __repr__(self):
        return {
            "name": self.name,
            "friends": self.friends,
            "movies": self.movies
        }

    def add_friend(self, friend):
        self.friends.append(friend)

    def add_movies(self, movie):
        self.movies.extend(movie)



