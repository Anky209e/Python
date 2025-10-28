# Implement Queue using Linked list


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return self.last

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
            return temp
        self.first = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    Queue1 = Queue(0)
    for i in range(1, 5):
        Queue1.enqueue(i)
    print("Before")
    Queue1.print_queue()
    print(Queue1.dequeue().value)

    print("Remaining")
    Queue1.print_queue()
