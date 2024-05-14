// BOJ_2563
// 색종이

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;


int main() {
    int n = 0, res = 0;
    cin >> n;
    vector<vector<int>> arr(101, vector<int>(101, 0));

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        for (int j = 0; j < 10; ++j) {
            for (int k = 0; k < 10; ++k) {
                if (arr[x + j][y + k] == 0) {
                    arr[x + j][y + k] = 1;
                }
            }
        }
    }

    for (int i = 1; i < 101; ++i) {
        for (int j = 1; j < 101; ++j) {
            if (arr[i][j] == 1)
                res++;
        }
    }

    cout << res;

    return 0;
}