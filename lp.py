# номер 5
# def f(x,y):
#     n = x
#     k = ''
#     while n > 0:
#         ost = n % y
#         n = n // 2
#         k = str(ost) + k
#     return k
# # for g in range(105,1000):
# g = 107
# g1 = f(g,2)
# c = 0
# g2 = g1
# while c < 3:
#     o_ = g2.count('0')
#     I_ = g2.count('1')
#     if o_ == I_:
#         g2 += g2[-1]
#         c += 1
#     elif o_ > I_:
#         g2 += '1'
#         c += 1
#     elif I_ > o_:
#         g2 += '0'
#         c += 1
# g3 = int(g2,2)
# print(g3)
# if g3 % 4 == 0:
#     print(g3)








# номер 6
# v = 0
# def f(s):
#     global v
#     s = 3 * (s // 10)
#     n=1
#     while s < 221:
#         s = s + 13
#         n = n * 2
#     if n == 256:
#         v += 1
# for k in range(1,1000000):
#     f(k)
# print(v)

# номер 10
#
# alf = ['В','А','Л','Е','Р','И','Я']
# alf.sort()
# v = 1
# for x in alf:
#     for y in alf:
#         for z in alf:
#             g = x+y+z
#             if g.count('В') == 1:
#                 print(v,g)
#                 v +=1







# номер 11
# alf = ['Р','У','С','Л','А','Н']
# v = 0
# for f1 in alf:
#     for f2 in alf:
#         for f3 in alf:
#             for f4 in alf:
#                 for f5 in alf:
#                     g = f1+f2+f3+f4+f5
#                     if g.count('У') <= 1 and g.count('А') <= 1:
#                         print(g)
#                         v += 1
# print(v)


# номер 15
# for i in range(201,1000):
#     n = '1'
#     n = n*i
#     while '111' in n or '222' in n:
#         if '111' in n:
#             n = n.replace('111','22',1)
#         if '222' in n:
#             n = n.replace('222','1',1)
#     if n.count('1') == 0:
#         print(i)
#         print(n)

# номер 18
# def f(x,A):
#     return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))
# for A in range(10000):
#     if all(f(x,A) for x in range(1000)):
#         print(A)

# номер 19
# def f(n):
#     if n == 0: return 0
#     elif n > 0 and n%2==0: return f(n/2)
#     elif n%2==1: return 1 + f(n-1)
#
# for n in range(1,900+1):
#     if f(n) == 9:
#         print(n)


# номер 20
# with open('17.txt') as f:
#     max_ = 0
#     l = []
#     m = 0
#     for j in f:
#         l.append(int(j))
#     for k in range(len(l)-1):
#         a = l[k]
#         b = l[k+1]
#         if a % 3 == 0 or b % 3 == 0:
#             m += 1
#             if a + b > max_:
#                 max_ = a  + b
# print(m,max_)

# номер 22
# def f(x,p):
#     if x >= 68 and p == 3:
#         return True
#     else:
#         if x < 68 and p == 3:
#             return False
#         else:
#             if x >= 68:
#                 return False
#     return  f(x+1,p+1) or f(x+4,p+1) or f(x*5,p+1)
#
#
# for j in range(1,67+1):
#     if f(j,1):
#         print(j)



# номер 23
# def f(x,y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x+1,y) + f(x*3,y)
# print(f(2,28)+f(28,90))
# print(f(2,90))


# номер 24
# with open('24.txt') as f:
#     d_count = 0
#     a = f.readline().strip()
#     v = 0
#     max_ = 0
#     for k in range(len(a)):
#         if a[k] != 'D':
#             v+=1
#         elif a[k] == 'D':
#             d_count += 1
#             if d_count > 1:
#                 max_ = max(max_,v)
#                 v = 0
#                 d_count = 0
#             elif d_count <= 1:
#                 v+=1
# print(max_)