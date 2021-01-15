def binarySearch(a, low, high, key):
    while low <= high:
        mid = (low+high)//2
        if a[mid]<key:
            low = mid + 1
        elif a[mid] > key:
            high = mid-1
        else:
            return mid
    return -1

a = [1,2,3,4,5,6,7,8,9]
print("Key Index: ", binarySearch(a, 0, len(a), 8))

'''
Key Index:  7
'''