# encoding:utf8
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


# 冒泡排序优化：用Flag避免数组已经有序的情况
def BubbleSort2(arr):
    n = len(arr)
    Flag = True
    for i in range(n):
        if not Flag:
            break
        Flag = False
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                Flag = True
    return arr


# 最优时间复杂度 O(n^2)， 最差时间复杂度 O(n)
if __name__ == "__main__":
    arr = [6, 3, 2, 5, 1, 6, 3]
    print(BubbleSort(arr))
