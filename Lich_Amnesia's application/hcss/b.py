# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-16 21:44:48
# @Last Modified time: 2016-11-16 23:01:08
# @FileName: b.py

# Complete the function below.

import collections
def  countCharacters(strings,  multiples):
    n = len(strings)
    ans = []
    for i in range(n):
        dic = collections.Counter(strings[i])
        res = 0
        for j in dic:
            if dic[j] % multiples[i] == 0:
                res += 1
        print dic
        ans.append(res)
    return ans

strings = ["avcsddd", "sdw2dd3"]
multiples = [3, 1]


print countCharacters(strings, multiples)