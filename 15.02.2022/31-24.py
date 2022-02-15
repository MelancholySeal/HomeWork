with open('k7b-5.txt') as f:
    for line in f:
        a = line.strip()
ex = 'CA'
ind = 0
v = 0
max_ = 0
for letter in a:
    if letter == ex[ind]:
        ind += 1
        v += 1
        ind = ind%2
        max_ = max(v,max_)
    elif letter == 'B':
        ind = 1
        v = 1
    else:
        v = 0
        ind = 0
print(max_)