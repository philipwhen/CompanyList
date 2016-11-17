/*
* @Author: Lich_Amnesia
* @Date:   2016-11-16 18:02:07
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-11-16 18:10:26
*/

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

char uperCase(char ch)
{
    if(ch >= 'a' && ch <= 'z') return ch - 'a' + 'A';
    return ch;
}

string solution(string &S, int K) {
    // write your code in C++11 (g++ 4.8.2)
    string mask = "";
    for (char chr : S) {
        if(chr != '-') mask += uperCase(chr);
    }
    vector<char> ans;
    int len = mask.size();
    int ptr = 1;
    while(len - ptr >= 0)
    {
        ans.push_back(mask[len-ptr]);
        if(ptr != len && ptr % K == 0) ans.push_back('-');
        ptr ++;
    }
    return string(ans.rbegin(), ans.rend());
}

int main(){
    string s = "sa-SS";
    int k = 2;
    cout << solution(s, k) << endl;
    return 0;
}