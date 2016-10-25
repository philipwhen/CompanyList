# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-22 20:35:44
# @Last Modified by:   lich
# @Last Modified time: 2016-10-22 20:35:44


# Complete the function below.


def  arrangeCoins(coins):
    for coin in coins:
        le = 0
        ri = 1000000000
        while le <= ri:
            mid = (le + ri) / 2
            num = (1 + mid) * mid / 2
            if num <= coin:
                le = mid + 1
            else:
                ri = mid - 1
        print(le - 1)
