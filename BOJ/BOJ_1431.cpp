// BOJ_1431
// 시리얼 번호

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(string x, string y) {
    if (x.size() != y.size()) {
        if (x.size() < y.size()) {
            return true;
        } else {
            return false;
        }
    } else {
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < x.size(); i++) {
            if ('0' <= x[i] && x[i] <= '9') {
                sum1 += x[i] - '0';
            }
            if ('0' <= y[i] && y[i] <= '9') {
                sum2 += y[i] - '0';
            }
        }
        if (sum1 == sum2) {
            for (int i = 0; i < x.size(); i++) {
                if (x[i] != y[i]) {
                    return x[i] < y[i];
                }
            }
            return true;
        } else {
            return sum1 < sum2;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 0;
    cin >> n;

    vector<string> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end(), compare);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << '\n';
    }

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
