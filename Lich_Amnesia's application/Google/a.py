# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-16 17:50:26
# @Last Modified time: 2016-11-16 18:46:09
# @FileName: a.py

import random
num = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','0','1','2','3','4','5','6','7','8','9']
s = []
for i in range(0, 10000):
    s.append(random.choice(num))
print(''.join(s))