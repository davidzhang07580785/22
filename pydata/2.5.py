def bubble_sort(arr):
    n = len(arr)

    # 遍历数组元素
    for i in range(n):
        # 每次遍历将最大的元素移动到末尾
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # 打印每次遍历后的数组状态
        print(f"第 {i + 1} 次遍历后的数组: {arr}")


# 测试代码
arr = [64, 34, 25, 12, 22, 11, 90]
print("初始数组:", arr)
bubble_sort(arr)
print("排序后的数组:", arr)