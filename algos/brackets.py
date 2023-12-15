s = "()[]]{}"

def isValid(s):
    stack = []

    for bracket in s:
        if bracket in "([{":
            stack.append(bracket)
        elif bracket in ")]}":
            if len(stack) == 0:
                return False
            top = stack.pop()
            if bracket == ")" and top != "(":
                return False
            if bracket == "]" and top != "[":
                return False
            if bracket == "}" and top != "{":
                return False
    return not stack

print(isValid(s))
        