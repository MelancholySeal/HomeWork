with open('17-5.txt') as f:
    list_ = []
    for line in f:
        a = line.strip()
        list_.append(int(a))
max = 0
v = 0
for ind in range(len(list_)-1):
    if list_[ind]%2 == 0 or list_[ind+1]%2 == 0:
        v += 1
        if list_[ind] + list_[ind+1] > max:
            max = list_[ind] + list_[ind+1]
print(v,max)