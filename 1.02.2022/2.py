with open('26.txt') as f:
    pair = f.readline().split()
    pair = list(map(int,pair))
    n,m = pair[0],pair[1]
    list_ = []
    for k in range(n):
        a = f.readline().split()
        a[0] = int(a[0])
        list_.append(a)
list_.sort()
sum = []
mm = 0
ind = 0
mmm = 0
while mm <= m:
    sum.append(list_[ind])
    mmm = mm
    mm += list_[ind][0]
    ind += 1
ind2 = ind-1
while ind2 <= n:
    if 'B' in list_[ind2]:
        if mmm - list_[ind2][0] + list_[ind2+1][0] <= m: