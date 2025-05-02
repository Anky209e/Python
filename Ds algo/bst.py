import random


# commit check
class BST:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    #finding a value
    def find(self,value):
        if value < self.data:
            if self.left is None:
                return False
            return self.left.find(value)
        elif value > self.data:
            if self.right is None:
                return False
            return self.right.find(value)
        else:
            return True

    #printing
    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()
    
    # remove function(lol)
    def remove(self,data):
        #first case
        if self is None:
            return self
        #recursion for finding
        if data < self.data:
            self.left = self.left.remove(data)
            return self
        if data > self.data:
            self.right = self.right.remove(data)
            return self
        #checking for leafs
        if self.left is None and self.right is None:
            return None

        if self.left is None:
            temp = self.right
            self = None
            return temp
        if self.right is None:
            temp = self.left
            self = None
            return temp
        parent = self
        child = self.right
    
        while child.left != None:
            parent = child
            child = child.left

        if parent != self:
            parent.left = child.right
        else:
            parent.right = child.right
        
        self.data = child.data

        return self










rt = BST(20)
for i in range(0,10):
    a = random.randint(5,15)
    rt.insert(a)

rt.insert(1)
rt.insert(31)
rt.insert(8)
rt.insert(4)
rt.remove(4)
rt.show()
print(rt.find(31))
