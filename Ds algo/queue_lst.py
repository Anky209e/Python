class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def add(self,data):
        node_d = Node(data)


    def show(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    queue = Queue()
    for  i in range(2,3):
        queue.add(i)
queue.show()
