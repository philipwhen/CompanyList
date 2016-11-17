# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-28 20:13:16
# @Last Modified by:   lich
# @Last Modified time: 2016-10-28 21:29:34




ls = "Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg"

s = "Atvt hrqgse, Cnikg"
t = "Your friend, Alice"


val_list = []

for i in range(len(s)):
    if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z'):
        val = (26 + ord(s[i]) - ord(t[i])) % 26
        val_list.append(val)
print val_list, len(val_list)
val_list = [8, 2, 5, 1, 2, 2, 0]
# val_list = val_list[:-1]
ans = ''
cnt = 0
num_of_digit = 0
for i in range(len(ls)):
    if ls[i] >= 'A' and ls[i] <= 'Z':
        val = (ord(ls[i]) - ord('A') - val_list[cnt] + 26) % 26
        ans += chr(val + ord('A'))
        cnt += 1
        num_of_digit += 1
    elif ls[i] >= 'a' and ls[i] <= 'z':
        val = (ord(ls[i]) - ord('a') - val_list[cnt] + 26) % 26
        ans += chr(val + ord('a'))
        cnt += 1
        num_of_digit += 1
    else:
        ans += ls[i]

    if cnt >= len(val_list):
            cnt = 0

print ans
print num_of_digit