prices = [7,1,5,3,6,4]

def maxProfit(prices):
    '''
    left_pointer is buy price
    right pointer is sell price
    '''
    left_pointer,right_pointer = 0,1
    max_profit = 0

    while right_pointer < len(prices):

        if prices[left_pointer] < prices[right_pointer]:
            profit = prices[right_pointer]-prices[left_pointer]
            max_profit = max(max_profit,profit)
        else:
            left_pointer = right_pointer
        
        right_pointer += 1

    return max_profit

def maxProfit_2(prices) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            max_profit = max(max_profit,profit)
        return max_profit
                        

print(maxProfit(prices))
