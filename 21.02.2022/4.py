with open('26-23.txt') as f:
    a = list(map(int,f.readline().split()))
    n = a[0]
    money = a[1]
    a_list = []
    b_list = []
    for k in range(n):
        a = f.readline().split()
        a[0] = int(a[0])
        if a[1] == 'A':
            a_list.append(a[0])
        if a[1] == 'B':
            b_list.append(a[0])
a_list.sort()
b_list.sort()
sum = 0
ind = 0
while sum <= money:
    sum+=a_list[ind]
    ind+=1
sum1 = 0
ind1 = 0
while sum1 <= money:
    sum1+=a_list[ind1]
    ind1+=1
print(sum,sum1,ind1)