f = open('39764-17.txt')
list_ = []
v = 0
list2_ = []
for line in f:
    g = int(f.readline().strip())
    list_.append(g)
for ind in range(len(list_)-3):
    a = list_[ind]
    b = list_[ind+1]
    c = list_[ind+2]
    if a + b > c and a + c > b and b + c > a:
        if ((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((b**2 + c**2) == a**2):
            if list_[ind] not in list2_:
                list2_.append(list_[ind])
            if list_[ind+1] not in list2_:
                list2_.append(list_[ind+1])
            if list_[ind+2] not in list2_:
                list2_.append(list_[ind+2])
print(len(list2_))