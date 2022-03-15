with open('26.txt') as f:
    a = f.readline().strip().split()
    n,m = int(a[0]),int(a[1])
    list_ = []
    for k in range(n):
        pair = f.readline().split()
        pair[0] = int(pair[0])
        list_.append(pair)
list_.sort()
ind = 0
mm = 0
list_N = []
while ind <= n and mm+list_[ind][0] <= m:
    a = list_[ind]
    mm += a[0]
    ind+=1
    list_N.append(a)
list_B = []
ind2 = ind
while ind2 < n:
    if 'A' in list_[ind2][1]:
        list_B.append(list_[ind2])
    ind2+=1
a_count = 0
for k in range(len(list_N)):
    if 'A' in list_N[k][1]:
        a_count +=1
indB = 0
list_N.reverse()
mmm = mm
for i in range(len(list_N)):
    if (mmm - list_N[i][0])+list_B[indB][0] <= m and 'B' in list_N[i][1]:
        mmm = mmm - list_N[i][0] + list_B[indB][0]
        indB += 1
        a_count += 1
print(m-mmm,a_count)