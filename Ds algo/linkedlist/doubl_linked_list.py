class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def __len__(self):
        val = 0
        temp = self.head
        while(temp is not None):
            val = val+1
            temp = temp.next
        return val
    
    def at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head.prev
        self.head = new_node
    
    def insert(self,data,index):
        temp = self.head
        if index<1 or index > len(self):
            print("Out of index")
            return
        if index ==1:
            self.at_start(data)
            return
        else:
            while(index != 0):
                index -= 1

                if index ==1:
                    new_node = Node(data)
                    new_node.next = temp.next
                    new_node.prev = temp.prev
                    temp.next = new_node
                
                temp = temp.next
                if temp == None:
                    break
        return temp
    
    def remove(self,index):
        temp = self.head

        if index == 1:
            self.head = temp.next
            temp = None
        for i in range(index):
            temp = temp.next
            if temp == None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        node_nx = temp.next.next
        node_pre = temp.prev.prev
        temp.next = None
        temp.prev = None

        temp.next = node_nx
        temp.prev = node_pre



dlist1 = DList()
dlist1.head = Node(1)
second_n = Node(2)
third_n = Node(3)
fourth_n = Node(4)
fifth_n = Node(5)


#connection
dlist1.head.next = second_n
second_n.next = third_n
second_n.prev = dlist1.head

third_n.next = fourth_n
third_n.prev = second_n

fourth_n.next = fifth_n
fourth_n.prev = third_n

dlist1.at_start(10)
dlist1.insert(12, 3)
print(len(dlist1))
dlist1.remove(1)
dlist1.printlist()