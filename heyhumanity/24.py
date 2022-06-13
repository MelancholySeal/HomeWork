with open('24-164-1.txt') as f:
    a = f.read().strip().split()
max_ = 0
max_str = ''
max_b = ''
for i in range(len(a)):
    str_ = a[i]
    len_ = len(str_)
    ind = 0
    v = 1
    while ind < len(str_)-1:
        c1 = str_[ind]
        c2 = str_[ind+1]
        if c1 == c2:
            v+=1
            if max_ < v:
                max_ = v
                max_str = str_
                max_b = str_[ind]
        else:
            v = 1
        ind+=1
n = max_str
ind = 0
w = []
v = 1
while ind < len(n)-1:
    c1 = n[ind]
    c2 = n[ind+1]
    if c1 == c2:
        v+=1
    else:
        if v == 10:
            w.append(c1)
        v = 1
    ind+=1
M = 0
for f in range(len(a)):
    M = M+ a[f].count('M')
print(w,M)