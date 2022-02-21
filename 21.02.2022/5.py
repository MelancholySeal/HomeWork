with open('27_B.txt') as f:
    n =int( f.readline().strip())
    list_ = []
    for line in range(n):
        thirds = list(map(int,f.readline().strip().split()))
        list_.append(thirds)
sum = 0
for item in list_:
    item.sort()
    sum += item[-1]
    if (item[-1] - item[0])%109 != 0:
        min1 = item[-1] - item[0]
        min_ = min1
        if (item[-1] - item[1])%109 != 0:
            min2 = item[-1] - item[1]
            min_ = min(min1,min2)
print(sum-min_,sum-min_%109,)