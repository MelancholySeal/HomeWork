def f(x,y):
    if x == y: return 1
    if x < y: return 0
    return f(bin(int(x,2)-1)[2::],y) + f(x[1]+len(x)*'0',y)
print(f('1000000','1000'))