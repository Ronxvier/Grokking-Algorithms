def findSmallest(arr):
    smallest = arr[0]
    smallindex=0
    for i in range(0,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallindex = i
    return smallindex

def selection_sort(arr):
    sorted = []
    for i in range(len(arr)): # don't edit list as you iterate over it, for i in arr doesn't work here.
        smallest = findSmallest(arr)
        sorted.append(arr.pop(smallest)) # pop takes in index
    return sorted
arr = [5,4,20,300,40,50,20,10]
print(selection_sort(arr))
