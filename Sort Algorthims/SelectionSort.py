def SelectionSort(x):
    for i in range(len(x)):
        MinIdx = i
        for j in range(i+1,len(x)):
            if x[MinIdx] > x[j]:
                MinIdx = j
        x[i] , x[MinIdx] = x[MinIdx] , x[i]

    return x
