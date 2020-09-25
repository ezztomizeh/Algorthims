def find(x,key):
    n = len(x)
    found = False
    for i in range(n):
        if x[i] == key :
            found = True
    if found is True:
        return True
    else:
        return False

def MaxNumber(x):
    n = len(x)
    maxIdx = 0
    for i in range(n):
        if x[i] > x[maxIdx]:
            maxIdx = i
    return x[maxIdx]

def MinNumber(x):
    n = len(x)
    minIdx = 0
    for i in range(n):
        if x[i] < x[minIdx]:
            minIdx = i
    return x[minIdx]
