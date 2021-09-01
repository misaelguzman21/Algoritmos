def binary_search(lst, value):
    lo, hi = 0, len(lst)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] < value:
            lo = mid + 1
        elif value < lst[mid]:
            hi = mid - 1
        else:
            return mid
    return -1
    
l = [3, 6, 14, 16, 33, 55, 56, 89]
x = 16
print(binary_search(l,x))
# 6 (the index of the found element)