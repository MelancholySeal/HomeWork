alf = ['И','Н','Ф','А']
v=0
for c1 in alf:
    for c2 in alf:
        for c3 in alf:
            for c4 in alf:
                for c5 in alf:
                    for c6 in alf:
                        w = c1+c2+c3+c4+c5+c6
                        if w.count('Ф') == 2:
                            v+=1
print(v)