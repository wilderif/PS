// BOJ_28325
// 호숫가의 개미굴

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
    
    vector<bool> check(2 * n, true);

    uint64_t tmp, res = 0;
    for (int i = 0; i < n; ++i) {
        cin >> tmp;
        if (tmp) {
            check[i] = check[n + i] = false;
            res += tmp;
        }
    }

    int idx = 0;
    while (check[idx]) {
        idx ++;
        if (idx == n) {
            idx = 0;
            break;
        }
    }

    for (int i = idx; i < idx + n - 1; ++i) {
        if (check[i]) {
            res++;
            if (check[i + 1]) {
                check[i + 1] = false;
            }
        }
    }
    if (check[idx + n - 1] && !check[idx + n]) {
        res++;
    }

    cout << res;

    return 0;
}
