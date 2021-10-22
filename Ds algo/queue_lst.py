class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    # function for checking is it is empty
    def isEmpty(self):
        return self.head == None
    
    #adding item in queue
    def Enqueue(self,data):
        temp = Node(data)
        if self.tail == None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
    
    #removing item from queue
    def Dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is already empty.")
        temp = self.head
        self.head = temp.next
        if (self.head == None):
            self.tail = None
    #showing queue
    def show(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

my_queue = Queue()
my_queue.Enqueue(10)
my_queue.Enqueue(111)
my_queue.Enqueue(12)
my_queue.Enqueue(13)
my_queue.Enqueue(14)
my_queue.show()
my_queue.Dequeue()
my_queue.Dequeue()
print("------------")
my_queue.show()
