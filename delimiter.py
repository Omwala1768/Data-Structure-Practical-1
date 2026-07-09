def delimiter_matching(expression):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expression:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":
            if len(stack) == 0:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0

expression = input("Enter an expression: ")

if delimiter_matching(expression):
    print("Delimiters are Balanced.")
else:
    print("Delimiters are NOT Balanced.")
