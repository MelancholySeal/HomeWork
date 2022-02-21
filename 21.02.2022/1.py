with open('24.txt') as f:
    a = f.readline().strip()
v = 0
A_count = 0
E_count = 0
max_ = 0
for ind in range(len(a)):
    v += 1
    if a[ind] == 'A':
        A_count += 1
    elif a[ind] == 'E':
        if A_count >= 3:
            max_ = max(v,max_)
            v = 0
            A_count = 0
print(max_)