# encoding:utf8

from collections import deque

"""
堆排序思想：
首先将待排序的数组构造出一个大根堆
取出这个大根堆的堆顶节点(最大值)，与堆的最下最右的元素进行交换，然后把剩下的元素再构造出一个大根堆
重复第二步，直到这个大根堆的长度为1，此时完成排序。
"""

# 交换两个元素
def swap(l, i, j):
    l[i], l[j] = l[j], l[i]
    return l

# 调整堆
def heap_adjust(arr, start, end):
    temp = arr[start]
    i = start
    # 沿关键字较大的孩子结点（2i）向下筛选
    j = 2 * i
    # 遍历当前节点的孩子结点
    while j <= end:
        # 如果当前节点不是最后一个节点而且左孩子小于右孩子，记录较大值
        if j < end and arr[j] < arr[j + 1]:
            j += 1  # j 为关键字中较大的记录的下标
        if temp >= arr[j]:
            break
        else:
            arr[i] = arr[j]
            i = j
            j = 2 * i
    arr[i] = temp  # 交换两个数字


def heap_sort(arr):
    """
    由于堆排序是一种完全二叉树，数组下标是从0开始的，二叉树的节点从1开始，
    所以这里我们引入一个辅助空间，用deque追加一个辅助位
    """
    l = deque(arr)
    l.appendleft(0)
    # 引入了一个辅助空间，这里l_len的长度-1
    l_len = len(l) - 1
    # first_sort_count 是有孩子的节点
    first_sort_count = l_len // 2

    # 从后往前将序列调整为一个大根堆
    print(l)
    for i in range(first_sort_count, 0, -1):
        heap_adjust(l, i, l_len)
    print(l)

    # 从后往前将堆顶元素和堆末尾元素进行交换， 然后把剩下的元素调整为一个大根堆
    for i in range(l_len, 0, -1):
        # 将堆顶记录和当前未经排序的子序列的最后一个记录交换
        l = swap(l, 1, i)
        # 将[1 ~ i-1]重新调整为大顶堆
        heap_adjust(l, 1, i - 1)
    # print(l)
    return [l[i] for i in range(1, len(l))]


# 时间复杂度 O(nlogn)
if __name__ == '__main__':
    s = [1, 7, 3, 5, 4, 2, 5, 9, 4, 3, 5]
    res = heap_sort(s)
    print(res)
