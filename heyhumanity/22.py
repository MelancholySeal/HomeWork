def f(x):
    m=0
    s=0
    while x > 0:
        d=x%6
        s += d
        if d > m: m = d
        x = x // 6
    return m,s
for x in range(10000):
    c = f(x)
    c1,c2 = c[0],c[1]
    if c1 == 5 and c2 == 16:
        print(x)
        break