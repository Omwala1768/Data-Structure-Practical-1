print("Om Wala S119")

SIZE = 10
hash_table = [None] * SIZE


def hash_function(key):
    return key % SIZE


def insert(key, value):
    index = hash_function(key)

    if hash_table[index] is None:
        hash_table[index] = (key, value)
        print("Inserted:", key, "->", value)
    else:
        print("Index already occupied. Collision occurred.")


def delete(key):
    index = hash_function(key)

    if hash_table[index] is not None and hash_table[index][0] == key:
        hash_table[index] = None
        print("Deleted key:", key)
    else:
        print("Key not found.")


def traverse():
    print("\nHash Table:")
    for i in range(SIZE):
        if hash_table[i] is not None:
            print(i, ":", hash_table[i][0], "->", hash_table[i][1])
        else:
            print(i, ": Empty")


while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 3:
        traverse()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
