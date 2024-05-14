// BOJ_1149
// RGB거리

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <limits.h>
#include <cstdio>

using namespace std;


int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<vector<u_int64_t>> arr(n, vector<u_int64_t> (3, 0));

    int tmp;
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < 3; ++i) {
        cin >> tmp;
        arr[j][i] = tmp;
        }
    }

    for (int j = 1; j < n; ++j) {
        for (int i = 0; i < 3; ++i) {
            if (i == 0) {
                arr[j][i] += min(arr[j - 1][1], arr[j - 1][2]);
            }
            else if (i == 1) {
                arr[j][i] += min(arr[j - 1][0], arr[j - 1][2]);
            }
            else {
                arr[j][i] += min(arr[j - 1][0], arr[j - 1][1]);
            }
        }
    }
    

    cout << min(arr[n - 1][0], min(arr[n - 1][1], arr[n - 1][2]));

    return 0;
}