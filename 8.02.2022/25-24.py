with open('k7a-5.txt') as f:
    a = f.read().strip()
v = 0
max_ = 0
for ind in range(len(a)):
    if a[ind] != 'C' and a[ind] != 'F':
        v+=1
        max_ = max(v,max_)
    elif a[ind] == 'C' or a[ind] == 'F':
        v = 0
print(max_)