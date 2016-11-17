# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-16 23:01:14
# @Last Modified time: 2016-11-17 00:17:58
# @FileName: d.py

def  getMaxLakeVolume(heights, distances):
    n = len(heights)
    left = [(0, 0)] * n
    right = [(0, 0)] * n
    sum_ = [0] * n
    sumd = [0] * n
    water = 0
 
    left[0] = (0, heights[0])
    sum_[0] = heights[0]
    sumd[0] = 1
    for i in range(1, n):
        if left[i - 1][1] > heights[i]:
            left[i] = left[i-1]
        else:
            left[i] = (i, heights[i])
        sum_[i] = sum_[i - 1] + heights[i]
        sumd[i] = sumd[i - 1] + 1 + distances[i - 1]


    right[n-1] = (n - 1, heights[n-1])
    for i in range(n - 2, 0, -1):
        if right[i + 1][1] > heights[i]:
            right[i] = right[i + 1]
        else:
            right[i] = (i, heights[i])
        # right[i] = max(right[i+1], heights[i])

    ans = 0
    for i in range(0, n):
        h = min(right[i][1], left[i][1])
        r = right[i][0]
        l = left[i][0]
            
        if r == l: continue
        mini = sum_[r] - sum_[l] - heights[r]
        inter = sumd[r] - sumd[l] - 1
        print l, r, h, i, mini, inter
        ans = max(inter * h - mini, ans)
    return ans

h = [6,6,6,3,6]
d = [1,1,4,2]
h = [2,3,4,1]
d = [6,9,4]
print getMaxLakeVolume(h,d)

