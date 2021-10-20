class Queue:
    def __init__(self,arr=[]):
        self.arr = arr
    def show(self):
        print(self.arr)

    def enqueue(self,data):
        self.arr.append(data)
        return self.arr
    def dqueue(self):
        self.arr.remove(0)
        return self.arr
    def size(self):
        return len(self.arr)
    


queu = Queue()
for i in range(0,10):
    queu.enqueue(i)
queu.show()
queu.enqueue(123)
queu.show()
queu.dqueue()
queu.show()
