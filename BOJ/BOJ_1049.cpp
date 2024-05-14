// BOJ_1049
// 기타줄

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(const vector<int>& a, const vector<int>& b) {
    return a[1] < b[1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> arr(m, vector<int>(2, 0));
    for (int i = 0; i < m; i++) {
        cin >> arr[i][0] >> arr[i][1];
    }

    int min_6 = 0, min_0 = 0;
    sort(arr.begin(), arr.end());
    min_6 = arr[0][0];
    sort(arr.begin(), arr.end(), compare);
    min_0 = arr[0][1];

    if (min_6 > min_0 * 6) {
        cout << min_0 * n;
    } else {
        int res1 = 0, res2 = 0;
        if (n % 6) {
            res1 = min_6 * (n / 6 + 1);
            res2 = min_6 * (n / 6) + min_0 * (n % 6);
            cout << min(res1, res2);
        } else {
            cout << min_6 * (n / 6);
        }
    }

    return 0;
}