// BOJ_2535
// 아시아 정보올림피아드

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare (vector<int> a, vector<int> b) {
    return a[2] > b[2];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n = 0;
    cin >> n;
    vector<vector<int>> arr(n, vector<int> (4, 0));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> arr[i][j];
        }
    }

    sort(arr.begin(), arr.end(), compare);

    int tmp_1, tmp_2;
    tmp_1 = arr[0][0];
    tmp_2 = arr[1][0];

    cout << arr[0][0] << ' ' << arr[0][1] << '\n';
    cout << arr[1][0] << ' ' << arr[1][1] << '\n';

    if (tmp_1 == tmp_2) {
        for (int i = 2; i < n; ++i) {
            if (arr[i][0] != tmp_1) {
                cout << arr[i][0] << ' ' << arr[i][1];
                break;
            }
        }
    } else {
        cout << arr[2][0] << ' ' << arr[2][1];
    }

    return 0;
}