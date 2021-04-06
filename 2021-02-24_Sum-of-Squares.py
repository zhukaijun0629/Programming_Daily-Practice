"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a number n, find the least number of squares needed to sum up to the number.
"""


def square_sum(n):
    # Fill this in.
    dp = [1] * (n + 1)
    for num in range(1, n+1):
        if int(num ** 0.5) ** 2 == num:
            continue
        cur_min = float('inf')
        for child in range(1, num // 2 + 1):
            cur_min = min(cur_min, dp[child] + dp[num - child])
        dp[num] = cur_min
    return dp[n]

def square_sum2(n):
    visited = [0]*(n + 1)
    ans = float("inf")
    queue = [0]
    num_steps = 0
    visited[0] = 1
    while queue:
        next_queue = []
        for start in queue:
            target = n - start
            if target == 0:
                return num_steps
            i = 1
            while i * i <= target:
                next_start = start + i * i
                if next_start <= n and not visited[next_start]:
                    visited[next_start] = 1
                    next_queue.append(next_start)
                i += 1
        queue = next_queue
        num_steps += 1
    return num_steps




print(square_sum2(13))
# Min sum is 3^2 + 2^2
# 2
