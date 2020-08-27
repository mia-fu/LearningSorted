# encoding:utf8

def partition(arr, low, high):
    # 用数组中的第一个记录作为枢纽记录
    privotKey = arr[low]
    # 从数组的两端交替向中间扫描
    while low < high:
        while low < high and arr[high] >= privotKey:
            high -= 1
        # 将比枢纽小的数交换到低端
        arr[low], arr[high] = arr[high], arr[low]

        while low < high and arr[low] <= privotKey:
            low += 1
        # 将比枢纽大的数交换到高端
        arr[low], arr[high] = arr[high], arr[low]
    # 返回枢纽所在位置
    return low


def QuickSort(arr, low, high):
    if low < high:
        # 算出枢纽值，将数组一分为二
        privot = partition(arr, low, high)
        # 对低子表递归排序
        QuickSort(arr, low, privot - 1)
        # 对高子表递归排序
        QuickSort(arr, privot + 1, high)


# 最优时间复杂度 O(nlogn)， 最差时间复杂度 O(n^2)
# 最优空间复杂度 O(logn)， 最差空间复杂度 O(n)
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5, 2, 4, 6, 24]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)
