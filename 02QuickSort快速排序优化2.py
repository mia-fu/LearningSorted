# encoding:utf8

# 优化不必要的交换
def partition(arr, low, high):
    # 三数交换
    mid = low + (high - low) // 2
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[mid] > arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]


    while low < high:
        # 设置一个哨兵元素
        pivotKey = arr[low]
        while low < high and arr[high] >= pivotKey:
            high -= 1
        # 采用替换而不是交换
        arr[low] = arr[high]
        while low < high and arr[low] <= pivotKey:
            low += 1
        arr[high] = arr[low]
        arr[low] = pivotKey

    return low


def QuickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)


arr = [10, 7, 8, 9, 1, 5, 2, 4, 6, 2]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
