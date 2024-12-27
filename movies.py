FAVORITE_MOVIES = ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight']

def movies(favorite_movies):
    favorite_movies.append('The Godfather')
    favorite_movies.remove('The Matrix')
    print(f'Total number of movies: {len(favorite_movies)}')
    favorite_movies.sort()
    print("Your favorite movies in alphabetical order:")
    for movie in favorite_movies:
        print(f"- {movie}")

if __name__ == '__main__':
    movies(FAVORITE_MOVIES)