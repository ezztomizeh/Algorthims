'''
     0 1 2  3 4 5  6  7
X = [1,5,10,7,8,11,12,9]
n = 8
#for 1:

'''

def heapfity(x,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and x[i] < x[left]:
        largest = left

    if right < n and x[largest] < x[right]:
        largest = right

    if largest != i:
        x[i] , x[largest] = x[largest] , x[i]

        heapfity(x,n,largest)

def HeapSort(x):
    n = len(x)

    for i in range(n//2-1,-1,-1):
        heapfity(x,n,i)

    for i in range(n-1,0,-1):
        x[i],x[0] = x[0] , x[i]
        heapfity(x,i,0)
