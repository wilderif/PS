// BOJ_30970
// 선택의 기로

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool Compare_1 (const vector<int>& v1, const vector<int>& v2) {
    if (v1[0] > v2[0]) {
        return true;
    } else if (v1[0] == v2[0]) {
        if (v1[1] < v2[1]) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

bool Compare_2 (const vector<int>& v1, const vector<int>& v2) {
    if (v1[1] < v2[1]) {
        return true;
    } else if (v1[1] == v2[1]) {
        if (v1[0] > v2[0]) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 0;
    cin >> n;

    vector<vector<int>> arr(n, vector<int>(2));

    for (int i = 0; i < n; ++i) {
        cin >> arr[i][0];
        cin >> arr[i][1];
    }

    sort(arr.begin(), arr.end(), Compare_1);
    cout << arr[0][0] << ' ' << arr[0][1] << ' ' << arr[1][0] << ' ' << arr[1][1] << '\n';

    sort(arr.begin(), arr.end(), Compare_2);
    cout << arr[0][0] << ' ' << arr[0][1] << ' ' << arr[1][0] << ' ' << arr[1][1] << '\n';

    return 0;
}