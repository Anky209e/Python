#this is a function practice project and there are multi functions are used.
def sum():
    s1 = int(input("Enter no 1:\n"))
    s2 = int(input("Enter no 2:\n"))
    print("Sum of those no is",s1+s2)
def sub():
    su1 = int(input("Enter no 1:\n"))
    su2 = int(input("Enter no 2:\n"))
    print("Subtraction is",su1-su2)
def multi():
    mu1 = int(input("Enter the no 1:\n"))
    mu2 = int(input("Enter the no 2:\n"))
    print("Multiplication is",mu1*mu2)
def div():
    di1 = float(input("Enter uppervalue:\n"))
    di2 = float(input("Enter lowervalue:\n"))
    print("Answer is ",di1%di2)
def power():
    po1 = int(input("Enter the base value:\n"))
    po2 = int(input("Enter the power value:\n"))
    print("Answer is ",po1**po2)
print("WELCOME to pycal")
print("Enter one of following")

user = int(input("1)Sum of two no.\n2)Subtraction of two no.\n3)Multiplication of two no.\n4)Division of two no.\n5)Exponential value."))
if user == 1:
    sum()
elif user ==2:
    sub()
elif user == 3:
    multi()
elif user == 4:
    div()
elif user == 5:
    power()
else:
    print("Wrong input\n")