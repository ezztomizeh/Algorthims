def find(x,key):
    n = len(x)
    isFounded = False

    for i in range(n):
        if x[i] == key:
            isFounded = True
            if i != 0:
                x[i] , x[i-1] = x[i-1],x[i]

    return isFounded
