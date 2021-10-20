class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    #pushing elements in stack
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size+=1
    #checking if stack is empty
    def isEmpty(self):
        return self.size == 0
    #getting size of stack
    def getSize(self):
        return self.size
    # popping element from stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty you cant pop.")
        pop_element = self.head.next
        self.head.next = self.head.next.next
        self.size-=1
        return pop_element
    #peeking
    def peek(self):
        temp = self.head.next
        if self.isEmpty():
            raise Exception("Its all Empty like your brain.")
        return temp.data
    #printing stack
    def __str__(self):
        temp = self.head.next
        sp = ""
        while temp:
            sp += str(temp.data) + " "
            #itertaing through
            temp = temp.next
        return sp


stack = Stack()
for i in range(10,20):
    stack.push(i)
print(f"Stack: {stack}")
print(f"Pop: {stack.pop}")
print(f"After popping: {stack}")
print(f"Peek: {stack.peek()}")
print(f"Size: {stack.getSize()}")