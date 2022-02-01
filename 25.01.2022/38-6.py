def f(d):
    n = 24
    s = 12
    while s <= 3004:
        s=s+d
        n=n+3
    return n

for d in range(1,10000):
    if f(d) == 75:
        print(d)