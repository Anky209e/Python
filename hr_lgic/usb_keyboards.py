
# Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
"""
STATEMENT:A person wants to determine the most expensive computer 
keyboard and USB drive that can be purchased with a give budget. 
Given price lists for keyboards and USB drives and a budget,
find the cost to buy them. If it is not possible to buy both items, return 
"""
def getMoneySpent(keyboards, drives, b):
    # Sum prices Storage list
    all_vals = []

    for kp in keyboards:
        for dp in drives:

            # Summing all prices
            s = kp+dp

            # all sums less then budget b
            if s <= b:
                all_vals.append(s)

    final_ar = list(set(all_vals))
    
    # if we can't buy
    if len(final_ar) == 0:
        return -1
    return max(final_ar)

if __name__ == "__main__":

    keyboards = [3,1]
    drives = [5,2,8]
    b = 10
    print(getMoneySpent(keyboards,drives,b))