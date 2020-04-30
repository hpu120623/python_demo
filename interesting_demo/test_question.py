# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/2 10:37
'''
import itertools
import numpy as np


def max_num_k(nums, k):
    # 获取输入的k个最大值
    nums = sorted(list(set(nums)))[::-1]
    print(nums)
    print(nums[:k])


def str_result(test_data):
    # 字符串的所有排序
    res = set(itertools.permutations(test_data))
    print(list(map(lambda x: ''.join(x), res)))


def max_array(test_array):
    max_sum = 0
    x = 0
    y = 0
    shape = np.array(test_array).shape
    for i in range(shape[0] - 1):
        last_sum = test_array[i][0] + test_array[i+1][0]
        for j in range(1, shape[1]):
            sum = last_sum
            last_sum = test_array[i][j] + test_array[i + 1][j]
            sum +=last_sum
            print(sum, last_sum)
            if sum > max_sum:
                max_sum = sum
                x = i
                y = j

    print(f'{max_sum}: {x} {y}')
    return [
        [test_array[x][y -1],test_array[x][y]],
        [test_array[x + 1][y -1],test_array[x +1][y]]
    ]


if __name__ == '__main__':
    max_num_k([1, 2, 3, 6, 78, 94, 3, 2], 3)
    str_result(['a', 'b', 'c', 'd', 'f'])
    test_array = [
        [1, 2, 0, 3, 4],
        [2, 3, 4, 5, 1],
        [1, 1, 5, 3, 0]
    ]
    print(max_array(test_array))
