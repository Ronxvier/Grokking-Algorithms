def quicksort(arr):
    # Base Case
    if len(arr)<2:
        return arr
    # Recursive Case
    pivot = arr[0]
    less = []
    greater = []
    for el in arr[1:]: # ensure you start this @ 1
        if el < pivot:
            less.append(el)
        else:
            greater.append(el)
    result = quicksort(less)+[pivot,]+quicksort(greater)
    return result
foo = [0,10,9,8,4,5,1,2,5,2,0]
bar = [1,0]
print(quicksort())
