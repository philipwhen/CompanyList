# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-22 20:04:09
# @Last Modified by:   lich
# @Last Modified time: 2016-10-22 20:14:47


# Complete the function below.


def  missingWords(s, t):
    list_s = s.split()
    list_t = t.split()
    i = 0
    ans = []
    for j in range(len(list_t)):
        if list_t[j] != list_s[i]:
            i += 1
            ans.append(list_s[i])
    return ans
