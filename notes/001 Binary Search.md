## Abstract
Consider the case in which you have a list of sorted numbers, and a number you're trying to find. Instead of going through the entire array from start to finish to find your number, you pick the middle entry, check if your desired number is higher or lower, if higher, you pick the middle of the numbers higher than the median, if lower, you pick the middle of the numbers lower than the median, and repeat. This search has a $\log_{2}(n)$ time complexity.

## Binary Search in Python
The `binary_search` function takes a sorted array an dan item. If the item is in the array, the function returns its position. You'll keep track of what part of the array you have to search through.
You start with the entire array:
```python
low = 0
high = len(list) - 1
```

Each time you check the middle element:
```python
mid = (low + high) / 2 # ex.  (50 + 100) / 2 = 75 for middle, this just takes middle of low and high.
guess = list[mid] # guess is entry @ that index
```

```python
# Guess was too low, move low to mid
if guess < item:
	low = mid+1
```

```python
# Guess was too high, move high to mid
if guess > item:
	high = mid-1
```

**Full Code:**
```python
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

arr = [0,10,20,30,40,50,60,70]
print(binary_search(arr,30)) # 3
```

The reason that its "high -1 and " "low +1" is because mid itself cannot be the answer, so we exclude it from future searches.