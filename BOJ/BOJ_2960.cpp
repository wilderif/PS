// BOJ_2960
// 에라토스테네스의 체

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<bool> arr(n + 1, true);
    arr[0] = false;
    arr[1] = false;

    int cnt = 0;
    int res = 0;

    while (true) {
        for (int i = 2; i < n + 1; i++) {
            if (arr[i]) {
                for (int j = 1; i * j < n + 1; j++) {
                    if (arr[i * j]) {
                        arr[i * j] = false;
                        cnt++;
                    }
                    if (cnt == k) {
                        res = i * j;
                        break;
                    }
                }
                break;
            }
        }

        if (res) {
            cout << res;
            break;
        }
    }

    return 0;
}
