with open('17-7.txt') as f:
    a = f.read().strip().split()
    a = list(map(int,a))
v = 0
max_ = 0
for i in range(len(a)):
    c = oct(a[i])[2::]
    end = len(c)-1
    start = end-1
    if c[end] == '7' and c[start:end+1] !='27':
        v+=1
        max_ = max(max_,int(c))
print(v,int(str(max_),8))