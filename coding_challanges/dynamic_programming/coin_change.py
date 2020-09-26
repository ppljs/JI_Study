from collections import deque

def coinChange(coins, amount):
    if amount == 0:
    return 0

    coins = sorted(coins, reverse=True)
    smallest = get_coin_change(coins, amount)
    return len(smallest) if len(smallest) > 0 else -1

def get_coin_change(coins, amount):
    smallest = [[]]
    curr = []
    def calculate_smallest_coin_change(curr_coins):
        for index, coin in enumerate(curr_coins):
            curr.append(coin)
            coin_sum = sum(curr)
            if coin_sum == amount:
                if len(smallest[0]) == 0 or 0 < len(curr) < len(smallest[0]):
                    smallest[0] = curr.copy()
            elif coin_sum < amount:
                calculate_smallest_coin_change(curr_coins[index:])

            curr.pop()

    calculate_smallest_coin_change(coins)
    return smallest[0]
