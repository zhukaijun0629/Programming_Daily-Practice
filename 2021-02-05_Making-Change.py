"""
Given a list of possible coins in cents, and an amount (in cents) n, return the minimum number of coins needed to create the amount n. If it is not possible to create the amount using the given coin denomination, return None.
"""


def make_change(coins, n):
    # Fill this in.
    level = {0}
    seen = {0}
    number = 0
    while level:
        if n in level:
            return number
        nextLevel = set()
        for pre in level:
            for coin in coins:
                if pre + coin <= n:
                    nextLevel.add(pre + coin)
        level = nextLevel - seen
        seen = seen | level
        number += 1
    return -1


print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
print(make_change([1, 4, 5], 8))
# 2 coins (4+4)
