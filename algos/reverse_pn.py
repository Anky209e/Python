


def evalRPN(tokens):
    stack  = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a,b = stack.pop(),stack.pop()
            stack.append(int(b-a))
        elif token == "/":
            a,b = stack.pop(),stack.pop()
            stack.append(int(b / a))
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(token))
    return stack[0]

if __name__ == "__main__":
    tokens = ["4","13","5","/","+"]

    print(evalRPN(tokens))
        
