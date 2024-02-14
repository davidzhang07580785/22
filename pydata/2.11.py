def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 逐个取出堆顶元素，进行排序
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

        # 打印每次遍历后的数组状态
        print(f"第 {n - i} 次遍历后的数组: {arr}")


# 测试代码
arr = [64, 34, 25, 12, 22, 11, 90]
print("初始数组:", arr)
heap_sort(arr)
print("排序后的数组:", arr)