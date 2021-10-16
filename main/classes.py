class Item:
    pay_rate = 0.7
    def __init__(self,name:str,price:float,quantity=0):
        #validating values
        assert price>=0, f"Price {price} is not greather than zero"
        assert quantity>=0
        #assign the values
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item("candy",10,3)
# print(item1.name)
print(item1.price)
item1.apply_discount()
print(item1.price)
# print(item1.quantity)
# print(item1.calculate_total())

# print(Item.pay_rate)
# print(item1.pay_rate)

# print(Item.__dict__)
# print(item1.__dict__)





