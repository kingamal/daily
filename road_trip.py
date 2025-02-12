import random

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

def movie_night():
    print("🎬 Welcome to Movie Night Recommender! 🎬")
    print("Available genres: Action,Comedy, Drama, Sci-Fi, Horror")
    genre = input("Enter a genre: ").capitalize()
    if genre in movies:
        movie = random.choice(movies[genre])
        print(f"🍿 Tonight, let's watch '{movie}'.")
    else:
        print("❌ Sorry, that genre is not available. Try again!")

if __name__ == "__main__":
    movie_night()