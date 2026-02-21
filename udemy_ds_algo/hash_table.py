class HashTable:
    def __init__(self, size=10):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for c in key:
            hash = (hash + ord(c) * 23) % len(self.data_map)
        return hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        key_list = []
        for index in range(len(self.data_map)):
            if self.data_map[index] is not None:
                for i in range(len(self.data_map[index])):
                    key_list.append(self.data_map[index][i][0])
        return key_list

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}:{val}")


if __name__ == "__main__":
    htable = HashTable(size=10)
    htable.set_item("Bananas", 10)
    htable.set_item("bolts", 40)
    htable.set_item("washers", 8)
    htable.set_item("lumber", 70)
    htable.print_table()
    print(htable.get_item("bolts"))
    print(htable.get_item("hehe"))
    print(htable.keys())
