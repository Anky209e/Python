import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.arrHeap = [0]*(self.maxsize+1)
        self.arrHeap[0] = -1*sys.maxsize
        self.min = 1
        self.size = 0
    
    #Function to return left child
    def lchild(self,pos):
        return 2*pos
    
    #function to return right child
    def rchild(self,pos):
        return (2*pos)+1
    
    #function to return parent
    def parent(self,pos):
        return pos//2
    
    #function for returninng if node is leaf
    def isLeaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
    
    #function for swap
    def swap(self,firstp,secondp):
        self.arrHeap[firstp],self.arrHeap[secondp] = self.arrHeap[secondp],self.arrHeap[firstp]
    
    #heapifying the tree
    def Heapify(self,pos):
        # if node is non-leaf and greater than child(minheap)
        if not self.isLeaf(pos):
            if self.arrHeap[pos] > self.arrHeap[self.lchild(pos)] or self.arrHeap[pos] > self.arrHeap[self.rchild(pos)]:
                self.swap(pos,self.lchild(pos))
                self.Heapify(self.lchild(pos))

            #else swap with right child and heapfy
            else:
                self.swap(pos,self.rchild(pos))
                self.Heapify(self.rchild(pos))

    #printing heap
    def show(self):
        for i in range(1,(self.size//2)+1):
            print("Parent: "+str(self.arrHeap[i])+"\n"+"LChild: "+str(self.arrHeap[2*i])+"\n"+"RChild: "+str(self.arrHeap[2*i+1]))
    
    #inserting
    def insert(self,data):
        if self.size > self.maxsize:
            return
        self.size+=1
        self.arrHeap[self.size] = data
        temp = self.size
        while self.arrHeap[temp] < self.arrHeap[self.parent(temp)]:
            self.swap(temp,self.parent(temp))
            temp = self.parent(temp)
            
    #building heap with heapify
    def Heap(self):
        for i in range(self.size//2, 0, -1):
            self.Heapify(i)
    
    #removing and returning smallest
    def remove(self):
        delt = self.arrHeap[self.min] 
        self.arrHeap[self.min] = self.arrHeap[self.size]
        self.size-=1
        self.Heapify(self.min)
        return delt

myheap = MinHeap(20)
for j in range(1,11):
    myheap.insert(j)

myheap.Heap()

myheap.show()
print(myheap.remove())