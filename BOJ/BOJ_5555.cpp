// BOJ_5555
// 반지

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

bool find(string target, string in) {

    int i = 0, j = 0;
    while (1) {
        for (int k = 0; k < target.length(); ++k) {
            if (target[i + k] != in[j + k]) {
                j++;
                if (in[j] == '\0')
                    return false;
                break;
            }
            if (k == target.length() - 1)
                return true;
        }
    }
}


int main() {
    string s;
    cin >> s;
    int n = 0, res = 0;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        string tmp_s;
        cin >> tmp_s;
        tmp_s += tmp_s;
        if (find(s, tmp_s) == true) {
            res += 1;
        }
    }

    cout << res;

    return 0;
}