// BOJ_12788
// 제 2회 IUPC는 잘 개최될 수 있을까?

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    int goal = m * k;
    vector<int> arr(n, 0);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end(), greater<int>());

    int check = 0;
    for (int i = 0; i < n; i++) {
        check += arr[i];
        if (check >= goal) {
            cout << i + 1;
            return 0;
        }
        if (i == n - 1) {
            cout << "STRESS";
            return 0;
        }
    }

    return 0;
}