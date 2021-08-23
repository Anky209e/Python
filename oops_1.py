class Employees():
    def __init__(self, name, age, salary, leave):
        self.name = name
        self.age = age
        self.salary = salary
        self.leave = leave
    
    #class method
    def change_leaves(cls, new_leaves):
        cls.leave = new_leaves
    
    def print_details(self):
        return f"Name:{self.name}\nAge:{self.age}\nSalary:{self.salary}\nLeaves:{self.leave}"

Anky = Employees("Ankit", 18, "10lacs", 15)

print(Anky.print_details())

Anky.change_leaves(13)
print("---------------------\n")
print(Anky.print_details())