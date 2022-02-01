for k in range(652938,1744328+1):
    v = 0
    dels = []
    for del_ in range(1,k+1):
        if k%del_==0:
            v+= 1
            dels.append(del_)
            if v>5:
                break
    if v == 5:
        print(dels)
        print('-----')