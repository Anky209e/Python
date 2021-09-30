my_list =["books","pen","hdd","ram","laptop skin","pen drive"]
print(my_list)
num_list =[2,3,4,5,6,7]
print(num_list)
#arrange list in descending order
num_list.sort()
print(num_list)
#remove any item from list
num_list.remove(4)
print(num_list)
#arrange list in descending order
num_list.reverse()
print(num_list)
#add no to end of list
num_list.append(29)
print(num_list)
#list slicing
print(my_list[::2])
#insert no at a decided place in list.
num_list.insert(1,45)
print(num_list)
#pop no
num_list.pop()
print(num_list)
#tuple
tup_01 = (1,3,2,4)
print(tup_01)
#swapping two numbers.
a = 1
b = 4
a,b = b,a
print(a,b)
#Adds an element at the end of the list
my_list.append("added item")
print(my_list)
#Removes all the elements from the list
#my_list.clear()
#print(my_list)
#Returns a copy of the list
my_list.copy()
print(my_list)
#Returns the number of elements with the specified value
my_list.count("added item")
print(my_list)
#Add the elements of a list (or any iterable), to the end of the current list
my_list.extend("ex")
print(my_list)
#Removes the element at the specified position
my_list.pop(2)
print(my_list)