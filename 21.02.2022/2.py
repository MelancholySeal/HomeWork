for num in range(11000000,1000000000):
    n = 0
    mn = 0
    while n <= 2:
        del1 = 0
        del2 = 0
        for del_ in range(num-1,1,-1):
            if num%del_ == 0:
                del2 = del1
                del1 = del_
                n+=1
            mn = del1*del2
        if mn > 0 and mn < 10000:
            print(mn,num)