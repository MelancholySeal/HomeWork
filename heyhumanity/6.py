def f(s):
    n = 121
    while s < 124:
        s = s + 10
        n = n + 17
    return n
max_ = 0
for s in range(1000):
    if f(s)==291:
        if f(s) > max_:
            max_ = s
print(max_)