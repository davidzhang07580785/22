def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        # 打印每次遍历后的数组状态
        print(f"第 {i} 次遍历后的数组: {arr}")


# 测试代码
arr = [64, 34, 25, 12, 22, 11, 90]
print("初始数组:", arr)
insertion_sort(arr)
print("排序后的数组:", arr)