for x in range(100000000,300000000+1):
    for m in range(0,29,2):
        for n in range(1,18,1):
            N = (2**m)*(7**n)
            if N == x:
                print(x,m+n)
