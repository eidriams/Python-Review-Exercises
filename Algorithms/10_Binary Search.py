"""Implement Binary Search
Binary search is an O(log(n)) efficiency algorithm for searching a sorted array to find an element. 

It operates using the following steps:

Find the middle value of a sorted array. If value == target return true (The value has been found and the search is complete).
If middle value < target, search right half of array in next compare.
If middle value > target, search left half of array in next compare.
If after searching the whole array the value is not present, return false (The array has been searched and the value is not in the array).
As you can see, you are successively halving an array, which gives you the log(n) efficiency. For this challenge, 
we want you to show your work - how you got to the target value... the path you took!

Write a function binarySearch that implements the binary search algorithm on an array, returning the path you took 
(each middle value comparison) to find the target in an array.

The function takes a sorted array of integers and a target value as input. It returns an array containing (in-order) 
the middle value you found at each halving of the original array until you found the target value. The target value should be 
the last element of the returned array. If the value is not found, return the string Value Not Found.

For example, binarySearch([1,2,3,4,5,6,7], 5) would return [4,6,5].

For this challenge, when halving, you MUST use Math.floor() when doing division: Math.floor(x/2). This will give a consistent, testable path.

Note: The following array will be used in tests:

const testArray = [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 49, 70]

Tests:
1. binarySearch should be a function.
2. binarySearch(testArray, 0) should return [13, 5, 2, 0].
3. binarySearch(testArray, 1) should return [13, 5, 2, 0, 1].
4. binarySearch(testArray, 2) should return [13, 5, 2].
5. binarySearch(testArray, 6) should return the string Value Not Found.
6. binarySearch(testArray, 11) should return [13, 5, 10, 11].
7. binarySearch(testArray, 13) should return [13].
8. binarySearch(testArray, 70) should return [13, 19, 22, 49, 70]."""


testArray = [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 49, 70]

def binarySearch(arr,target):

    low = 0
    high = len(arr)-1
    path = []

    print("Looking for target →",target)

    while low <= high:

        mid = (low+high) // 2
        print(f"low={low} - mid={mid} - high={high}")

        if arr[mid] == target:

            path.append(arr[mid])
            print(path)
            return True
        
        elif arr[mid] < target:

            path.append(arr[mid])
            low = mid + 1
            print("low=",low)
        
        else:
            
            path.append(arr[mid])
            high = mid - 1
            print("high →",high)
    
    print(path)        

    return False



print(binarySearch(testArray, 0))
print("\n")
print(binarySearch(testArray, 1))
print("\n")
print(binarySearch(testArray, 2))
print("\n")
print(binarySearch(testArray, 6))
print("\n")
print(binarySearch(testArray, 11))
print("\n")
print(binarySearch(testArray, 13))
print("\n")
print(binarySearch(testArray, 70))
