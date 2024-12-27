def display_menu():
    print("\nPlease select an option:")
    print("1. Add a new movie")
    print("2. Remove a movie")
    print("3. Total number of favorite movies")
    print("4. The movies in alfabethical order")
    print("5. Exit")

def add_movie(movies):
    movie = input("Enter the new movie to add: ")
    movies.append(movie)

def remove_movie(movies):
    movie = input("Enter the movie to remove: ")
    movies.remove(movie)

def total_number(movies):
    print(f'Total number of movies: {len(movies)}')

def sorting_movies(movies):
    movies.sort()
    print("Your favorite movies in alphabetical order:")
    for movie in movies:
        print(f"- {movie}")

def main():
    movies = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_movie(movies)
        elif choice == 2:
            remove_movie(movies)
        elif choice == 3:
            total_number(movies)
        elif choice == 4:
            sorting_movies(movies)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == '__main__':
    main()