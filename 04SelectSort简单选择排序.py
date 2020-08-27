# encoding:utf8

def SelectSort(arr):
    # 记录每一个元素的下标
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]

    return arr


# 最优时间复杂度 O(1)， 最差时间复杂度 O(n^2)
if __name__ == '__main__':
    s = [1, 7, 3, 5, 4, 2, 5, 5]
    res = SelectSort(s)
    print(res)
