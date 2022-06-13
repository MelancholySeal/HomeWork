def f(n):
    a = n
    a = bin(a)[2::]
    if n%2==0:
        a = a + '01'
    else:
        a = a + '10'
    return int(a,2)
for x in range(1000):
    if f(x) > 81:
        print(f(x))
        break