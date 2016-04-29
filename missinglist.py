def missing_number(x,y):
    if len(x) and len(y) == 0:
        return 0

    if set(x).difference(y) == set(y).difference(x):
        return 0

    if len(x) < len(y):
        return set(y).difference(x)


print missing_number([],[])
print missing_number([1,2,3],[1,2,3])
print missing_number([1,2,3],[1,2,3,4])






def missing_number(x,y):
    if len(x) and len(y) == 0:
        return 0

    if len(x) == len(y):
        return 0
    else:
        for i in y:
            if i not in x:
                return i
