import time
from colorama import init, Fore, Style

init(autoreset=True)


class Player:
    def __init__(self, jersey_number):
        self.jersey_number = jersey_number
        self.next_player = None


class FootballTeam:
    def __init__(self):
        self.captain = None

    def sign_player_front(self, jersey_number):
        new_player = Player(jersey_number)
        new_player.next_player = self.captain
        self.captain = new_player

    def sign_player_end(self, jersey_number):
        new_player = Player(jersey_number)

        if self.captain is None:
            self.captain = new_player
            return

        current_player = self.captain

        while current_player.next_player:
            current_player = current_player.next_player

        current_player.next_player = new_player

    def sign_player_position(self, jersey_number, squad_position):
        new_player = Player(jersey_number)

        if squad_position == 0:
            new_player.next_player = self.captain
            self.captain = new_player
            return

        current_player = self.captain

        for _ in range(squad_position - 1):
            if current_player is None:
                raise IndexError("Position out of bounds.")
            current_player = current_player.next_player

        new_player.next_player = current_player.next_player
        current_player.next_player = new_player

    def release_player_number(self, jersey_number):
        current_player = self.captain

        if current_player is not None:
            if current_player.jersey_number == jersey_number:
                self.captain = current_player.next_player
                current_player = None
                return

        while current_player is not None:
            if current_player.jersey_number == jersey_number:
                break

            previous_player = current_player
            current_player = current_player.next_player

        if current_player is None:
            return

        previous_player.next_player = current_player.next_player
        current_player = None

    def release_player_position(self, squad_position):
        if self.captain is None:
            return

        current_player = self.captain

        if squad_position == 0:
            self.captain = current_player.next_player
            current_player = None
            return

        for _ in range(squad_position - 1):
            current_player = current_player.next_player

            if current_player is None or current_player.next_player is None:
                raise IndexError("Position out of bounds.")

        next_member = current_player.next_player.next_player
        current_player.next_player = None
        current_player.next_player = next_member

    def show_team(self):
        current_player = self.captain

        if current_player is None:
            print(Fore.RED + "No players are currently in the football team.")
            return

        print(Fore.GREEN + "Football Team Lineup:")

        while current_player:
            print(current_player.jersey_number, end=" ")
            current_player = current_player.next_player

        print()


def coach_menu():
    print("\n" + Style.BRIGHT + "==== Football Team Management ====")
    print("1. " + Fore.BLUE + "Sign Player at Beginning")
    print("2. " + Fore.BLUE + "Sign Player at End")
    print("3. " + Fore.BLUE + "Sign Player at Position")
    print("4. " + Fore.BLUE + "Release Player by Jersey Number")
    print("5. " + Fore.BLUE + "Release Player by Position")
    print("6. " + Fore.BLUE + "Display Team")
    print("7. " + Fore.RED + "Exit Match")


def football_manager():
    team = FootballTeam()

    while True:
        coach_menu()

        try:
            choice = int(input(Style.RESET_ALL + "Enter your choice: "))

            if choice == 1:
                jersey = int(input("Enter Jersey Number: "))
                team.sign_player_front(jersey)
                print(Fore.GREEN + "Player signed at the beginning of the lineup.")

            elif choice == 2:
                jersey = int(input("Enter Jersey Number: "))
                team.sign_player_end(jersey)
                print(Fore.GREEN + "Player signed at the end of the lineup.")

            elif choice == 3:
                jersey = int(input("Enter Jersey Number: "))
                position = int(input("Enter Squad Position (0-indexed): "))
                team.sign_player_position(jersey, position)
                print(Fore.GREEN + f"Player added at position {position}.")

            elif choice == 4:
                jersey = int(input("Enter Jersey Number to release: "))
                team.release_player_number(jersey)
                print(Fore.RED + "Player released from the team.")

            elif choice == 5:
                position = int(input("Enter Squad Position to release: "))
                team.release_player_position(position)
                print(Fore.RED + f"Player at position {position} released.")

            elif choice == 6:
                team.show_team()

            elif choice == 7:
                print(Style.RESET_ALL + "Full Time! Exiting Football Team Manager.")
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
    football_manager()
