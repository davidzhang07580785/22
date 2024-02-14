def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

# 测试代码
arr = [64, 34, 25, 12, 22, 11, 90]
print("初始数组:", arr)
arr = quick_sort(arr)
print("排序后的数组:", arr)