class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LList:
    def __init__(self):
        self.head = None

#function for showing list ie printing
    def showList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
# pushing element to start
    def atstart(self,data):
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

#adding element after a node

    def afternode(self,prev_node,data1):
        if prev_node is None:
            print("There is no previous node named")
            return
        else:
            new_node1 = Node(data1)
            new_node1.next = prev_node.next
            prev_node.next = new_node1
            
# adding node to last

    def at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node
    
#removing node
    def remove_node(self,value):
        temp = self.head

        if(temp is not None):
            if(temp.data == value):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == value:
                break
            prev_node = temp
            temp = temp.next
        if temp==None:
            return
        prev_node.next = temp.next
        temp=None

#getting length
    def len(self):
        val =  0
        temp = self.head
        while(temp is not None):
            val = val+1
            temp = temp.next
        return val

#insertion
    def insert(self,data,index):
        temp = self.head
        if (index < 1):
            print("Out of Index")
            return
        
        
        if index == 1:
            self.atstart(data)
        
        else:
            while (index != 0):          
                index -= 1
    
                if (index == 1):
                    new_node = Node(data)
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                
                temp = temp.next
                if temp == None:
                    break           
            if index > self.len():
                print("index out of range")       
        return temp
#deletion
    def delete(self,index):
        temp = self.head
        if (index < 1):
            print("Out of Index")
            return
        
        
        if index == 1:
            self.head = temp.next
            temp = None
            return
        
        for i in range(index):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        node_del = temp.next.next
        temp.next = None
 
        temp.next = node_del


linkedList = LList()

#creating nodes with data
linkedList.head = Node(29)
second_node = Node(11)
third_node = Node(18)
fourth_node = Node(44)


linkedList.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node


linkedList.atstart(99)
linkedList.atstart(991)
linkedList.at_end(16)
linkedList.remove_node(18)
# linkedList.afternode(second_node, 1)
# print(linkedList.len())
linkedList.insert(1, 111)
linkedList.delete(3)
linkedList.showList()