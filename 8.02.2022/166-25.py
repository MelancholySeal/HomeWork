for m in range(1,30+1,2):
    for n in range(0,11+1,2):
        num = (2**m) * (7**n)
        if num >= 100000000 and num <= 300000000:
            print(num,m+n)