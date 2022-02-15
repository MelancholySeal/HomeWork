with open('17-10.txt') as f:
    list = []
    for line in f:
        a = int(line.strip())
        list.append(a)
def f(x):
    list_ = []
    n = len(x)
    ind = 0
    while ind <= n-3:
        a = x[ind]
        b = x[ind+1]
        c = x[ind+2]
        ind += 1
        n_list = []
        if a + b > c and a + c > b and b + c > a:
            if c > a and c > b:
                if c ** 2 < a ** 2 + b ** 2:
                    n_list.append(a)
                    n_list.append(b)
                    n_list.append(c)
                    list_.append(n_list)
            elif a > c and a > b:
                if a**2 < c**2 + b**2:
                    n_list.append(a)
                    n_list.append(b)
                    n_list.append(c)
                    list_.append(n_list)
            elif b > c and b > a:
                if b ** 2 < c ** 2 + a ** 2:
                    n_list.append(a)
                    n_list.append(b)
                    n_list.append(c)
                    list_.append(n_list)
    return list_
print(len(f(list)))