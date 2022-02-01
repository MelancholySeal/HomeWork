def f(n):
    string = '3'*11+'5'*n
    while '53' in string:
        string = string.replace('53','8',1)
    return string
for n in range(1,10000):
    string = f(n)
    if sum(map(int,string)) == 118:
        print(n)