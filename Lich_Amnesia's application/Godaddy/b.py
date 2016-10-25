# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-22 20:21:24
# @Last Modified by:   lich
# @Last Modified time: 2016-10-22 20:26:37


def rearrangeWord(word):
    if not word:
        return None
    length = len(word)
    i = length - 2
    while i >= 0:
        if ord(word[i]) < ord(word[i + 1]):
            break
        i -= 1
    if i == -1:
        return None
    for j in range(i + 1, length):
        if j == length - 1:
            break
        if ord(word[j]) > ord(word[i]) and ord(word[i]) >= ord(word[j + 1]):
            break
    tmp = word[i]
    word[i] = word[j]
    word[j] = tmp
    word[i + 1:length] = word[length - 1:i:-1]

    return word
