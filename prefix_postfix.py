def prefix_to_postfix(prefix):
    stack = []
    for ch in reversed(prefix):
        if ch.isdigit():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            postfix = op1 + op2 + ch
            stack.append(postfix)

    return stack.pop()

def evaluate_postfix(postfix):
    stack = []
    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
            elif ch == '^':
                stack.append(a ** b)

    return stack.pop()

prefix = input("Enter Prefix Expression: ")
postfix = prefix_to_postfix(prefix)
print("Postfix Expression:", postfix)
result = evaluate_postfix(postfix)
print("Result:", result)
