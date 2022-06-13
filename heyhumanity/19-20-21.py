print('task 19')
def f(x,p):
    if x >= 50 and p == 3:
        return True
    else:
        if x < 50 and p == 3:
            return False
        else:
            if x >= 50:
                return False
    if p%2==0:
        return f(x+2,p+1) or f(x*3,p+1)
    else:
        return f(x+2,p+1) and f(x*3,p+1)
for x in range(1,49+1):
    if f(x,1):
        print(x)
        break

print('task 20')
def f(x,p):
    if x >= 50 and p == 4:
        return True
    else:
        if x < 50 and p == 4:
            return False
        else:
            if x >= 50:
                return False
    if p%2==1:
        return f(x+2,p+1) or f(x*3,p+1)
    else:
        return f(x+2,p+1) and f(x*3,p+1)
for x in range(1,49+1):
    if f(x,1):
        print(x)

print('task 21')
def f(x,p):
    if x >= 50 and (p == 5 or p == 3):
        return True
    else:
        if x < 50 and p == 5:
            return False
        else:
            if x >= 50:
                return False
    if p%2==0:
        return f(x+2,p+1) or f(x*3,p+1)
    else:
        return f(x+2,p+1) and f(x*3,p+1)
for x in range(1,49+1):
    if f(x,1):
        print(x)
print('-------')
def f(x,p):
    if x >= 50 and p == 3:
        return True
    else:
        if x < 50 and p == 3:
            return False
        else:
            if x >= 50:
                return False
    if p%2==0:
        return f(x+2,p+1) or f(x*3,p+1)
    else:
        return f(x+2,p+1) and f(x*3,p+1)
for x in range(1,49+1):
    if f(x,1):
        print(x)