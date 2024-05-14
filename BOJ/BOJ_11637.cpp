// BOJ_11637
// 인기 투표

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
        int n = 0, total = 0, most = 0, most_idx = 0;
        cin >> n;
        vector<int> arr(n, 0);

        int tmp;
        for (int j = 0; j < n; ++j) {
            cin >> tmp;
            arr[j] = tmp;
            total += tmp;
            if (tmp > most) {
                most = tmp;
                most_idx = j;
            }
        }

        for (int j = most_idx; j < n; ++j) {
            if (j != most_idx && arr[j] == most) {
                cout << "no winner" << '\n';
                break;
            }

            if (j == n - 1) {
                if (most > total / 2) {
                    cout << "majority winner " << most_idx + 1 << '\n';
                } else {
                    cout << "minority winner " << most_idx + 1 << '\n';
                }
            }
        }
    }

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
