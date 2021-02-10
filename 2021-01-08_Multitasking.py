"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)
"""
def findTime(arr, cooldown):
    # Fill this in.
    mp = {}
    timer = 0
    for task in arr:
        if task not in mp or mp[task] <= 0:
            for key,value in mp.items():
                mp[key] = value - 1
            mp[task] = cooldown
            timer += 1
            continue
        if mp[task] > 0:
            cooldown_left = mp[task]
            timer += cooldown_left
            for key,value in mp.items():
                mp[key] = value - cooldown_left
            timer += 1
            mp[task]=cooldown
    return timer

def findTime2(arr, cooldown):
    # Fill this in.
    res = []
    if not arr:
        return 0
    res = [arr[0]]
    for task in arr[1:]:
        if task not in res[-1:-1-cooldown:-1]:
            res.append(task)
        else:
            index = res[-1:-1-cooldown:-1].index(task)
            cooldown_left = cooldown - index
            res.extend(['_']*cooldown_left + [task])
        print(res)
    return len(res)


print (findTime2([1, 1, 2, 1], 2))
# 7
