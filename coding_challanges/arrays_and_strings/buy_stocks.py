def maxProfit(prices):
    if not prices:
        return 0
    max_profit = 0
    max_value = prices[-1]
    for i in range(len(prices) - 2, -1, -1):
        if prices[i] > max_value:
            max_value = prices[i]
        else:
            curr_profit = max_value - prices[i]
            if curr_profit > max_profit:
                max_profit = curr_profit
    
    return max_profit


if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
