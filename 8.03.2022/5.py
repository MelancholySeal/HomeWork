def f(x,y,A):
    return ((x<5) <= (x**2<=A)) and ((y**2<=A) <= (y<=5))
v = 0
for A in range(1,10000):
    if all(f(x,y,A) for x in range(1000) for y in range(1000)):
        v+=1
print(v)