def binary_search(arr, target):
    high = len(arr)-1
    low = 0
    while high>=low:
        mid = int((high+low)/2)
        guess = arr[mid]
        if guess < target:
            low = mid+1
        elif guess > target:
            high = mid-1
        else:
            return mid
