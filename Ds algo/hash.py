class HashMap:
    def __init__(self,maxsize=100):
        self.maxsize = maxsize
        self.arr = [None]*maxsize
        self.hstore = []

    def enHash(self,key):
        dtypes = [int,str]
        if type(key) not in dtypes:
            print("Only accepted datatype for keys are:",dtypes)
            return
        elif type(key) == str:
            sum_val = 0
            for ch in key:
                sum_val+=ord(ch)
            fnl_hash = (sum_val % self.maxsize)
            return fnl_hash
        else:
            return key % self.maxsize



    def insert(self,key,data):
        hash = self.enHash(key)
        if self.arr[hash] is not None:
            hash = self.enHash(hash)+1
        if self.arr[self.maxsize-1] is not None:
            self.maxsize = self.maxsize+3
        self.hstore.append(hash)
        self.arr[hash] = data
    
    def find(self,key):
        hash = self.enHash(key)
        return self.arr[hash]
    
    def show(self):
        print(self.arr)

if __name__=="__main__":
    mymap = HashMap(10)
    mymap.insert("kitna","hello")
    mymap.insert("kitna","hi")
    mymap.insert("sarthak","Hithere")
    mymap.insert("swaksh","itsokey")
    # print(mymap.find("ankit"))
    # print(mymap.find("sarthak"))
    # print(mymap.find("swaksh"))
    mymap.show()



