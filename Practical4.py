import time
from colorama import init, Fore, Style

init(autoreset=True)


class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id
        self.next_movie = None
        self.previous_movie = None


class MovieCollection:
    def __init__(self):
        self.first_movie = None

    def add_movie_front(self, movie_id):
        new_movie = Movie(movie_id)

        if self.first_movie is None:
            self.first_movie = new_movie
        else:
            new_movie.next_movie = self.first_movie
            self.first_movie.previous_movie = new_movie
            self.first_movie = new_movie

    def add_movie_end(self, movie_id):
        new_movie = Movie(movie_id)

        if self.first_movie is None:
            self.first_movie = new_movie
        else:
            current_movie = self.first_movie

            while current_movie.next_movie:
                current_movie = current_movie.next_movie

            current_movie.next_movie = new_movie
            new_movie.previous_movie = current_movie

    def add_movie_position(self, movie_id, position):
        if position == 0:
            self.add_movie_front(movie_id)
            return

        new_movie = Movie(movie_id)
        current_movie = self.first_movie

        for _ in range(position):
            if current_movie is None:
                raise IndexError("Position out of bounds.")
            current_movie = current_movie.next_movie

        if current_movie is None:
            raise IndexError("Position out of bounds.")

        new_movie.next_movie = current_movie
        new_movie.previous_movie = current_movie.previous_movie

        if current_movie.previous_movie:
            current_movie.previous_movie.next_movie = new_movie

        current_movie.previous_movie = new_movie

    def remove_first_movie(self):
        if self.first_movie is None:
            return

        if self.first_movie.next_movie is None:
            self.first_movie = None
        else:
            self.first_movie = self.first_movie.next_movie
            self.first_movie.previous_movie = None

    def remove_last_movie(self):
        if self.first_movie is None:
            return

        if self.first_movie.next_movie is None:
            self.first_movie = None
        else:
            current_movie = self.first_movie

            while current_movie.next_movie:
                current_movie = current_movie.next_movie

            current_movie.previous_movie.next_movie = None

    def remove_movie_position(self, position):
        if self.first_movie is None:
            return

        current_movie = self.first_movie

        for _ in range(position):
            if current_movie is None:
                raise IndexError("Position out of bounds.")
            current_movie = current_movie.next_movie

        if current_movie is None:
            raise IndexError("Position out of bounds.")

        if current_movie.previous_movie:
            current_movie.previous_movie.next_movie = current_movie.next_movie

        if current_movie.next_movie:
            current_movie.next_movie.previous_movie = current_movie.previous_movie

    def show_movies(self):
        current_movie = self.first_movie

        if current_movie is None:
            print(Fore.RED + "Movie Collection is empty.")
            return

        print(Fore.GREEN + "Movie Collection:")

        while current_movie:
            print(current_movie.movie_id, end=" ")
            current_movie = current_movie.next_movie

        print()

    def search_movie(self, movie_id):
        current_movie = self.first_movie

        while current_movie:
            if current_movie.movie_id == movie_id:
                return True
            current_movie = current_movie.next_movie

        return False

    def total_movies(self):
        current_movie = self.first_movie
        count = 0

        while current_movie:
            count += 1
            current_movie = current_movie.next_movie

        return count


def cinema_menu():
    print("\n" + Style.BRIGHT + "~~~~ Movie Collection Manager ~~~~")
    print("1. " + Fore.BLUE + "Add Movie at Beginning")
    print("2. " + Fore.BLUE + "Add Movie at End")
    print("3. " + Fore.BLUE + "Add Movie at Position")
    print("4. " + Fore.BLUE + "Remove First Movie")
    print("5. " + Fore.BLUE + "Remove Last Movie")
    print("6. " + Fore.BLUE + "Remove Movie at Position")
    print("7. " + Fore.BLUE + "Display Movie Collection")
    print("8. " + Fore.BLUE + "Search Movie")
    print("9. " + Fore.BLUE + "Total Movies")
    print("10. " + Fore.RED + "Exit")


def movie_manager():
    collection = MovieCollection()

    while True:
        cinema_menu()

        try:
            choice = int(input(Style.RESET_ALL + "Enter your choice: "))

            if choice == 1:
                movie = int(input("Enter Movie ID: "))
                collection.add_movie_front(movie)
                print(Fore.GREEN + "Movie added at the beginning.")

            elif choice == 2:
                movie = int(input("Enter Movie ID: "))
                collection.add_movie_end(movie)
                print(Fore.GREEN + "Movie added at the end.")

            elif choice == 3:
                movie = int(input("Enter Movie ID: "))
                position = int(input("Enter Position (0-indexed): "))
                collection.add_movie_position(movie, position)
                print(Fore.GREEN + f"Movie inserted at position {position}.")

            elif choice == 4:
                collection.remove_first_movie()
                print(Fore.RED + "First movie removed.")

            elif choice == 5:
                collection.remove_last_movie()
                print(Fore.RED + "Last movie removed.")

            elif choice == 6:
                position = int(input("Enter Position to remove: "))
                collection.remove_movie_position(position)
                print(Fore.RED + f"Movie at position {position} removed.")

            elif choice == 7:
                collection.show_movies()

            elif choice == 8:
                movie = int(input("Enter Movie ID to search: "))

                if collection.search_movie(movie):
                    print(Fore.GREEN + "Movie found in collection.")
                else:
                    print(Fore.RED + "Movie not found.")

            elif choice == 9:
                print(Fore.BLUE + f"Total Movies: {collection.total_movies()}")

            elif choice == 10:
                print(Style.RESET_ALL + "Closing Movie Collection Manager...")
                break

            else:
                print(Fore.YELLOW + "Invalid choice. Please try again.")

        except ValueError:
            print(Fore.YELLOW + "Please enter a valid integer.")

        except IndexError as error:
            print(Fore.RED + f"Error: {error}")

        except Exception as error:
            print(Fore.RED + f"Error: {error}")

        time.sleep(1)


if __name__ == "__main__":
    movie_manager()
