from collections import deque, Counter
from person import Person

class MovieNetwork():
    def __init__(self):
        self.people = {}

    def add_person(self, person: Person):
        self.people[person.name] = person

    def get_most_popular_movie(self, person_name):
        if person_name not in self.people:
            return None
        visited = set()
        queue = deque()
        movie_counter = Counter()

        queue.append(self.people[person_name])
        visited.add(person_name)

        while queue:
            current = queue.popleft()
            movie_counter.update(current.movies)

            for friend in current.friends:
                if friend.name not in visited:
                    visited.add(friend.name)
                    queue.append(friend)

        if not movie_counter:
            return None
        
        return f"Most popular movie : {movie_counter.most_common(1)[0][0]}"

