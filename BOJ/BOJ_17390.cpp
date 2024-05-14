// BOJ_17390
// 이건 꼭 풀어야 해!

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<uint64_t> arr(n + 1, 0);

    for (int i = 1; i < n + 1; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());
    for (int i = 1; i < n + 1; i++) {
        arr[i] += arr[i - 1];
    }

    while (q--) {
        int a, b;
        cin >> a >> b;
        cout << arr[b] - arr[a - 1] << '\n';
    }

    return 0;
} 