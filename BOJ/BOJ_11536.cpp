// BOJ_11536
// 줄 세우기

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<string> arr(n);
    vector<string> cmp(n);

    string tmp = "";
    for (int i = 0; i < n; ++i) {
        cin >> tmp;
        arr[i] = cmp[i] = tmp;
    }

    sort(cmp.begin(), cmp.end());

    for (int i = 0; i < n; ++i) {
        if (arr[i] != cmp[i]) {
            break;
        }
        if (i == n - 1) {
            cout << "INCREASING";
            return 0;
        }
    }

    for (int i = 0; i < n; ++i) {
        if (arr[i] != cmp[n - i - 1]) {
            break;
        }
        if (i == n - 1) {
            cout << "DECREASING";
            return 0;
        }
    }

    cout << "NEITHER";

    return 0;
}
