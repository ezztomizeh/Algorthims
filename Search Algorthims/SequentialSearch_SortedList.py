def find(x,key,biger):
    n = len(x)
    isFounded = False
    for i in range(n):
        if x[i] < biger:
            if x[i] == key:
                isFounded = True
        else:
            break

    return isFounded
