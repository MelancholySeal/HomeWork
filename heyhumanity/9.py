with open('9-114.txt') as f:
    w = []
    for n in range(5000):
        a = f.readline().strip().split()
        a = list(map(int,a))
        w.append(a)
v = 0
for i in range(len(w)):
    c1 = w[i][0]
    c2 = w[i][1]
    c3 = w[i][2]
    if c1==c2==c3:
        v+=1
print(v)