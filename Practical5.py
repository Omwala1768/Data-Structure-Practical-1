import os
import time
from colorama import Fore, Style, init

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
        init(autoreset=True)

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print(Fore.RED + "Queue is Full , Cannot Enqueue Item")
        else :
            self.queue.append(item)
            print(Fore.GREEN + f"Enqueued Item {item} in Queue")
            time.sleep(1)

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Cannot Dequeue Item, Queue is empty")
            return None
        else :
            item = self.queue.pop(0)
            print(Fore.YELLOW + f"Dequeued Item {item} from Queue")
            time.sleep(1)

    def front(self):
        if self.is_empty():
            print(Fore.RED + "Queue is Empty")
            return None
        print(Fore.MAGENTA + f"Front of the Queue is {self.queue[0]}")
        return self.queue[0]

    def traverse(self):
        if self.is_empty():
            print(Fore.RED + "Queue is Empty")
            return None
        else :
            print(Fore.BLUE + "Queue Contains : " , end=" ")
            for item in self.queue:
                print(Fore.BLUE + str(item), end=" ", flush=True)
                time.sleep(0.5)
            print()
        time.sleep(1)

    def display_queue(self):
        if self.is_empty():
            print(Fore.RED + "Queue is Empty")
        else :
            print(Fore.CYAN + "Displaying Queue : ")
            for index, item in enumerate(self.queue):
                print(Fore.CYAN + f"{index + 1}. {item}")
                time.sleep(0.5)
            time.sleep(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    max_size = int(input(Fore.GREEN + "Enter the maximum size of your Queue : "))
    q = Queue(max_size)

    while True :
        clear_screen()
        print(Fore.CYAN + "==== Om Wala S119 Queue Operation Menu ====")
        print(Fore.CYAN + "1. Enqueue")
        print(Fore.CYAN + "2. Dequeue")
        print(Fore.CYAN + "3. Front")
        print(Fore.CYAN + "4. Traverse")
        print(Fore.CYAN + "5. Display Queue")
        print(Fore.CYAN + "6. Check if Queue is Full")
        print(Fore.CYAN + "7. Check if Queue is Empty")
        print(Fore.CYAN + "8. Exit")
        user_input = input(Fore.RED + "Enter your choice (1-8) : ")

        if user_input == '1':
            item = int(input(Fore.YELLOW + "Enter Item to Enqueue in Queue : "))
            q.enqueue(item)
        elif user_input == '2':
            q.dequeue()
        elif user_input == '3':
            q.front()
        elif user_input == '4':
            q.traverse()
        elif user_input == '5':
            q.display_queue()
        elif user_input == '6':
            if q.is_empty :
                print(Fore.RED + "Queue is Empty")
            else :
                print(Fore.GREEN + "Queue is Not Emp")
        elif user_input == '7':
            if q.is_full():
                print(Fore.RED + "Queue is Full")
            else :
                print(Fore.GREEN + "Queue is Not Full")
        elif user_input == '8':
            break
        else :
            print(Fore.RED + "Invalid Choice , Try Again !")
        input(Fore.GREEN + "Press Enter to Continue")

    clear_screen()
    print(Fore.RED + "Terminating the Program")
