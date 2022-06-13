def f(x,n):
    a = x
    w = ''
    while a > 0:
        ost = a%n
        a = a//n
        w = w+str(ost)
    return w[::-1]
n = 7**2103-6*7**1270+3*5**57-98
print(sum(map(int,f(n,7))))