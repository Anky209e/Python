# Implement Stack
# using singly linked list


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def peek(self):
        if self.length == 0:
            return None
        return self.top

    def is_empty(self):
        if self.length == 0:
            return True
        return False


if __name__ == "__main__":
    Stack1 = Stack(0)
    for i in range(1, 5):
        Stack1.push(i)
    print("Before")
    Stack1.print_stack()
    print("After")
    print(Stack1.pop().value)
    print("Remaining Stack")
    Stack1.print_stack()
