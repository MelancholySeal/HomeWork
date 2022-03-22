with open('26-62.txt') as f:
    a = f.readline().strip().split()
    n,m= int(a[0]),int(a[1])
    l = []
    for k in range(n):
        g = f.readline().strip().split()
        g[0] = int(g[0])
        l.append(g)
l.sort()
mm = 0
ind = 0
ll = []
b_count = 0
while mm + l[ind][0] <= m:
    mm += l[ind][0]
    ll.append(l[ind])
    ind += 1
    if "Q" in l[ind][1]:
        b_count +=1
ind2 = ind
bl = []
while ind2 < len(l):
    if 'Q' in l[ind2][1]:
        bl.append(l[ind2])
    ind2+=1
indb = 0
mmm = mm
bl.sort()
ll.sort()
ll.reverse()
for inda in range(len(ll)):
    if "Z" in ll[inda][1]:
        if mmm - ll[inda][0] + bl[indb][0] <= m:
            mmm = mmm - ll[inda][0] + bl[indb][0]
            b_count +=1
            indb +=1
print(m-mmm,b_count)