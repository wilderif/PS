// BOJ_11501
// 주식

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

    int t = 0;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n = 0;
        cin >> n;
        vector<int> arr(n, 0);

        for (int j = 0; j < n; ++j) {
            cin >> arr[j];
        }

        uint64_t res = 0;
        int cur_max = 0;
        int idx = n - 1;
        for (int j = n - 1; j >= 0; --j) {
            if (arr[j] >= cur_max || j == 0) {
                for (int k = j; k < idx; ++k) {
                    if (cur_max - arr[k] > 0) {
                        res += cur_max - arr[k];
                    }
                }
                cur_max = arr[j];
                idx = j;
            }
        }

        cout << res << '\n';
    }


    return 0;
}