# with open('27-52a.txt') as f:
#     n = int(f.readline().strip())
#     l = []
#     for k in range(n):
#         l.append(int(f.readline().strip()))
# l.sort()
# l.reverse()
# ind = 0
# while ind < n-2:
#     if (l[ind]+l[ind+1]+l[ind+2])%3==0:
#         print(l[ind]+l[ind+1]+l[ind+2])
#         ind+=1
with open('27-52b.txt') as f:
    n = int(f.readline().strip())
    l = []
    for k in range(n):
        l.append(int(f.readline().strip()))
l.sort()
l.reverse()
ind = 0
while ind < n-2:
    if (l[ind]+l[ind+1]+l[ind+2])%3==0:
        print(l[ind]+l[ind+1]+l[ind+2])
        ind+=1