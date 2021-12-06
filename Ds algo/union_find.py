class union:
    def __init__(self):
        self.parent = {}

    def add(self,uni):
        for i in  uni:
            self.parent[i] = i
    def find(self,p):
        if self.parent[p]==p:
            return p
        return self.find(self.parent[p])

    def sSets(self):
        print([self.find(i) for i in self.parent])

    def union(self,f,s):
        x = self.find(f)
        y = self.find(s)
        self.parent[x] = y

if __name__ == "__main__":

    test = [1,2,3,4,5]
    my = union()
    my.add(test)

    my.sSets()
    my.union(1,2)
    my.sSets()