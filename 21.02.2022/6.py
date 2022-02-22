with open('111.txt') as f:
    n = int(f.readline().strip())
    list_ = []
    for k in range(n):
        pair = list(map(int,f.readline().split()))
        list_.append(pair)
list_.sort()
list_.reverse()
ind = 0
while ind <= n:
    if list_[ind][0] == list_[ind+1][0]:
        if (list_[ind][1] - list_[ind+1][1]) == abs(3):
            print(list_[ind][0],list_[ind][1],list_[ind+1][1],list_[ind][1] - list_[ind+1][1])
            break
    ind += 1