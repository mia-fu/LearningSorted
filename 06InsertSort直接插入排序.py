# encoding:utf8

def insert_sort(arr):
    for i in range(1, len(arr)):
        # 保存当前元素的值，依次比较选择
        key = arr[i]
        # 从当前记录开始往前进行比较
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 记录后移
            j -= 1
        arr[j + 1] = key  # 插入到正确的位置

    return arr


# 时间复杂度 O(n^2)
if __name__ == '__main__':
    arr = [1, 7, 3, 5, 4, 2, 5, 9, 4, 3, 5]
    res = insert_sort(arr)
    print(res)
