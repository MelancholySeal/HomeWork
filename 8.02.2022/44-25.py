f = []
for num in range(4837177,4837236+1):
    dels = 0
    for del_ in range(2,num):
        if num%del_ == 0:
            dels +=1
        if dels >= 1:
            break
    if dels == 0:
        f.append(num)

print(f)