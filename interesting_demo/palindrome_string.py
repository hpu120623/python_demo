# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/13 11:36
'''

# python实现回文字符串
def str_solution(test_str):
    s = list(test_str)
    l = len(s)
    dp = [[0] * l for i in range(l)]
    for i in range(l):
        dp[i][i] = True
        # 当 k = 2时要用到
        dp[i][i - 1] = True
    resLeft = 0
    resRight = 0
    # 枚举子串的长度
    for k in range(2, l + 1):
        # 子串的起始位置
        for i in range(0, l - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                # 保存最长的回文起点和终点
                if resRight - resLeft + 1 < k:
                    resLeft = i
                    resRight = j
    return ''.join(s[resLeft:resRight + 1])

if __name__ == '__main__':
    test_str = 'abcded,132reaaer234,9230-qrjrflksamnfcklv'
    print(str_solution(test_str))
