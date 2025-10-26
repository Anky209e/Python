class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Creating DoublyLinkedList


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Pops and returns Last element"""
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp

    def prepend(self, value):
        """Prepends a node"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return temp

    # TODO: Add get method for DoublyLinkedList

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # for the first half
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            return temp
        # for second half
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp


list1 = DoublyLinkedList(7)
list1.append(8)
list1.append(10)
list1.append(12)
# print(list1.pop_first().value)
print(list1.get(1).value)
print(list1.get(3).value)
# list1.print_list()
