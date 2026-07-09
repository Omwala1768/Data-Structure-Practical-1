stack = []
while True:
    print("\n----- MENU -----")
    print("1. Type Text")
    print("2. Undo")
    print("3. Show Current Text")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text: ")
        stack.append(text)
        print("Text Added.")

    elif choice == "2":
        if len(stack) == 0:
            print("Nothing to Undo!")
        else:
            removed = stack.pop()
            print("Removed:", removed)

    elif choice == "3":
        if len(stack) == 0:
            print("Current Text: Empty")
        else:
            print("Current Text:", " ".join(stack))

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
