def f(x,y,z,w):
    return int((w <= y) and ((x <= z) == (y <= x)))


print('x y z w | F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x,y,z,w,'|',f(x,y,z,w))


# x y z w | F
# 0 0 1 0 | 1
# 1 0 1 0 | 1
# 1 1 1 0 | 1