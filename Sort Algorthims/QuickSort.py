'''
  0  1  2  3  4
[ 4, 3, 1, 5, 6]
i = -1 = 6
Pivot = 5
j = 0
x[0] = 4
pivot = 5
[6,3,1,5,4]
j = 1
x[1] = 3
i = 0
[3,6,1,5,4]
j = 2
i = 1
[3,1,6,5,4]
j = 3
i = 2
[3,1,5,6,4]
j = 4
i = 3
[3,1,5,4,6]
i = 4
high = 5
[3,1,5,4,6]
'''
def Partition(x,low,high):
    i = (low-1)
    Pivot = x[high]

    for j in range(low,high):

        if x[j] <= Pivot:
            i += 1
            x[i] , x[j] = x[j] , x[i]

    x[i+1] , x[high] = x[high] , x[i+1]

    return (i+1)


def QuickSort(x,low,high):

    if len(x) == 1:
        return x

    if low < high:
        pi = Partition(x,low,high)

        QuickSort(x,low,pi-1)
        QuickSort(x,pi+1,high)
