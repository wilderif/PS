// BOJ_17404
// RGB거리 2

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n = 0;
    cin >> n;
    vector<vector<uint64_t>> arr(n, vector<uint64_t> (3, 0));
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < 3; ++i) {
            cin >> arr[j][i];
        }
    }

    vector<vector<uint64_t>> mem(n, vector<uint64_t> (3, 0));
    uint64_t res = 1000 * 1000 + 1;
    for (int k = 0; k < 3; ++k) {
        for (int i = 0; i < 3; ++i) {
            if (i == k) {
                mem[0][i] = arr[0][i];
            } else {
                mem[0][i] = 1001;
            }
        }
        for (int j = 1; j < n; ++j) {
            for (int i = 0; i < 3; ++i) {
                mem[j][i] = min(arr[j][i] + mem[j - 1][(i + 1) % 3],
                                arr[j][i] + mem[j - 1][(i + 2) % 3]);
            }
        }

        for (int i = 0; i < 3; ++i) {
            if (i != k){
                res = min(res, mem[n - 1][i]);
            }
        }
    }

    cout << res;

    return 0;
}
