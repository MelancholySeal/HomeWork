with open('27-63a.txt') as f:
    n = int(f.readline().strip())
    l = f.read().strip().split()
    l = list(map(int,l))
ind = 0
min_ = 1000000
for c1 in range(len(l)-3):
    for c2 in range(c1+1,len(l)-2):
        for c3 in range(c2+1,len(l)-1):
            for c4 in range(c3+1,len(l)):
                cc1 = l[c1]
                cc2 = l[c2]
                cc3 = l[c3]
                cc4 = l[c4]
                if (cc1+cc2+cc3+cc4)%9!=0:
                    min_ = min(min_,cc1+cc2+cc3+cc4)
print(min_)