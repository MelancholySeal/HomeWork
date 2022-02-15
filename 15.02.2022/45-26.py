f = open('26-45.txt')
n = int(f.readline().strip())
list_ = []
for line in range(n):
    a = int(f.readline().strip())
    list_.append(a)
list_.sort()
even2 = []
for a in range(n):
    for b in range(a+1,n):
        k = list_[a]
        k2 = list_[b]
        if (k + k2)%2 == 0:
            even = []
            even.append(k)
            even.append(k2)
            even.append((int((k+k2)/2)))
            even2.append(even)