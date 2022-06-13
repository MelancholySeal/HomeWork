p = {1,2,3,4,5,6}
q = {3,5,15}
def f(x,A):
    global p,q
    return (x not in A) <= ((x not in p)and(x in q)or(x not in q))
a = []

def g(n):
    global a
    for x in range(1,n):
        a.append(x)
for n in range(1,10000):
    g(n)
    if all(f(x,a) for x in range(1000)):
        print(n)
        break
