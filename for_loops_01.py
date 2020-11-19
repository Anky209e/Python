list1 = [["ankit",2],["capti",2],"silver","dingo"]
# for items, numbers in list1:
#     print(items,"and no is",numbers)
for items, numbers in list1:
    if numbers.isnumeric():
        print(items)
    