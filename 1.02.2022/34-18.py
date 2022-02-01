with open('18-16.csv') as f:
    list_ = []
    for k in f:
        a = k.strip()
        list_.append(int(a))
print(list_)