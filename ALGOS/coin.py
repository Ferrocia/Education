def min_coins(money):
    coins = [1, 3, 4]
    dp = [0] + [float('inf')] * money

    for x in range(1, money + 1):
        for c in coins:
            if x >= c:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[money]

print(min_coins(6))
print(min_coins(34))
print(min_coins(2))
print(min_coins(9))