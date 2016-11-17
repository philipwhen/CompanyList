/*
* @Author: Lich_Amnesia
* @Date:   2016-11-16 18:20:05
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-11-16 18:20:09
*/

#include <iostream>

using namespace std;

int dfs(tree * root, int A, int B, int &lbound, int &rbound, int &ans) {
    lbound = root->x;
    rbound = root->x;
    int sumNodes = 1;
    if (root->l != NULL) {
        int tl, tr;
        sumNodes += dfs(root->l, A, B, tl, tr, ans);
        lbound = min(lbound, tl);
    }
    if (root->r != NULL) {
        int tl, tr;
        sumNodes += dfs(root->r, A, B, tl, tr, ans);
        rbound = max(rbound, tr);
    }
    if (lbound >= A && rbound <= B) ans = max(ans, sumNodes);
    return sumNodes;
}
int solution(int A, int B, tree * T) {
    if (T == NULL) return 0;
    int l, r, ans = 0;
    dfs(T, A, B, l, r, ans);
    return ans;
}

int main(){

    return 0;
}