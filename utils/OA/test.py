import itertools

for a, b, *rest in itertools.permutations([1,2]):
    print(a,b,rest)