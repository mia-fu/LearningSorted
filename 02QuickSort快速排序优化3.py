# encoding:utf8

# 优化递归
def partition(arr, low, high):
    # 三数取中
    mid = low + (high - low) // 2
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[mid] > arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]

    pivotKey = arr[low]
    # 设置哨兵元素
    pre = pivotKey

    while low < high:
        while low < high and arr[high] >= pivotKey:
            high -= 1
        arr[low] = arr[high]

        while low < high and arr[low] <= pivotKey:
            low += 1
        arr[high] = arr[low]
        arr[low] = pre

    return low

def QuickSort(arr, low, high):
    while low < high:
        pivot = partition(arr, low, high)
        # 对低子表递归排序
        QuickSort(arr, low, pivot - 1)
        # 尾递归
        low = pivot + 1

arr = [10, 7, 8, 9, 1, 5, 2, 4, 6, 13, 4]
QuickSort(arr, 0, len(arr) - 1)
print(arr)