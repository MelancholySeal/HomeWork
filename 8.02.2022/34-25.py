max_ = {}
for num in range(586132,586430+1):
    dels = []
    for del_ in range(1, num):
        if num%del_ == 0:
            dels.append(del_)
            dels.sort()
    if len(dels) == 23:
        max_[num] = dels
print(len(max_[586140]),max_[586140][-1],max_[586140][-2])
print(len(max_[586140]),max_[586140][-1],max_[586140][-2])