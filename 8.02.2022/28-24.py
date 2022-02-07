with open('k7b-2.txt') as f:
    a = f.read().strip()
v = 0
max_ = 0
ind = 0
for k in range(len(a)):
    g = a[ind]
    if a[ind] == 'D':
        v += 1
        max_ =max(max_, v)
        if ind < len(a)-1:
            ind += 1
        else: break
        if a[ind] == 'B':
            v += 1
            max_ =max(max_, v)
            if ind < len(a)-1:
                ind += 1
            else:
                break
            if a[ind] == 'A':
                v += 1
                max_ =max(max_, v)
                if ind < len(a)-1:
                    ind += 1
                else:
                    break
                if a[ind] == 'C':
                    v += 1
                    max_ = max(max_, v)
                    if ind < len(a)-1:
                        ind += 1
                    else:
                        break
                else:
                    v = 0
                    ind += 1
            else:
                v = 0
                ind += 1
        else:
            v = 0
            ind += 1
    else:
        v = 0
        ind += 1
print(max_)