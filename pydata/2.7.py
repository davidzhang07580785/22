def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # 打印每次遍历后的数组状态
        print(f"第 {i + 1} 次遍历后的数组: {arr}")


# 测试代码
arr = [64, 34, 25, 12, 22, 11, 90]
print("初始数组:", arr)
selection_sort(arr)
print("排序后的数组:", arr)