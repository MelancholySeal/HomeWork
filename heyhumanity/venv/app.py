a = range(1000, 9999+1)

for k in a:
    list_ = []
    k = str(k)
    sum1 = int(k[0]) + int(k[1])
    list_.append(sum1)
    sum2 = int(k[1]) + int(k[2])
    list_.append(sum2)
    sum3 = int(k[2]) + int(k[3])
    list_.append(sum3)
    list_.sort()
    bg, lt = list_[2], list_[1]
    w = str(lt) + str(bg)
    if int(w) == 1315:
        print(k, w)
