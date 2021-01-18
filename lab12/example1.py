def minIndex( a , i , j ): 
    if i == j: 
        return i 
 
    k = minIndex(a, i + 1, j) 

    return (i if a[i] < a[k] else k) 

def Select_sort(a, n, index = 0): 
    if index == n: 
        return -1

    k = minIndex(a, index, n-1) 

    if k != index: 
        a[k], a[index] = a[index], a[k] 

    Select_sort(a, n, index + 1) 

elements = [22,8,12,-4,27,30,36,50,7,68,91,56,2,85,42,98,25] 
n = len(elements) 

Select_sort(elements, n) 

for i in elements: 
    print(i, end = ' ') 