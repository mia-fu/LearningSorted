# encoding:utf8

def shell_sort(arr):
    # 设定一个定长
    step = len(arr) // 3
    while step > 0:
        for i in range(step, len(arr)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and arr[i-step] > arr[i]:
                arr[i], arr[i-step] = arr[i-step], arr[i]
                i -= step
        step = step // 3
    return arr

# 时间复杂度 O(n^2)
if __name__ == '__main__':
    arr = [1, 7, 3, 5, 4, 2, 5, 9, 9, 3, 5]
    res = shell_sort(arr)
    print(res)