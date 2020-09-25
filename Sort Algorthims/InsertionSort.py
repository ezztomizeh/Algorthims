#Expalin how the code is working 
'''
i = 1
key = 1
j = 0

[4,1,3,2]
[1,4,3,2]
i = 2
key = 3
j = 1
[1,3,4,2]
j = 0
[1,3,4,2]
i = 3
key = 2
j = 2
[1,3,2,4]
j = 1
[1,2,3,4]
j = 0
[1,2,3,4]
Finshed
'''

def InsertionSort(x):
    for i in range(1,len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1

        x[j+1] = key

    return x
