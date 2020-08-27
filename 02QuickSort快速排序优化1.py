# encoding:utf8

# 优化选取枢纽，选取的枢纽值决定交换次数，我们尽量将枢纽值取到数组的中间位置
# 选择三数取中，即取三个关键字先进行排序，将中间数作为枢纽。
def partition(arr, low, high):
    mid = low + (high - low) // 2
    # 交换左端与右端，保证左端较小
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    # 交换中间与右端数据，保证中间较小
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # 交换中间与左端数据，保证左端较小
    if arr[mid] > arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
    # 此时low是三个数中的中间值

    pivotKey = arr[low]
    while low < high:
        if low < high and arr[high] >= pivotKey:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]

        if low < high and arr[low] <= pivotKey:
            low += 1
        arr[low], arr[high] = arr[high], arr[low]

    return low


def QuickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)


arr = [10, 7, 8, 9, 1, 5, 2, 4, 6, 24]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
