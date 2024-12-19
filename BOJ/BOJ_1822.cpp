// BOJ_1822
// 차집합

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <limits.h>
#include <cstdio>

using namespace std;


int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int a, b, idx_a = 0, idx_b = 0, res_count = 0;
    cin >> a >> b;
    vector<long long> arr_a(a);
    vector<long long> arr_b(b);
    vector<long long> res;

    for (int i = 0; i < a; ++i) {
        int tmp;
        cin >> tmp;
        arr_a[i] = tmp;
    }

    for (int i = 0; i < b; ++i) {
        int tmp;
        cin >> tmp;
        arr_b[i] = tmp;
    }

    sort(arr_a.begin(), arr_a.end());
    sort(arr_b.begin(), arr_b.end());

    while (1) {
        if (idx_a == a)
            break;
        // if (idx_b == b) {

        // }

        if (idx_b == b || arr_a[idx_a] < arr_b[idx_b]) {
            res.push_back(arr_a[idx_a]);
            res_count++;
            idx_a++;
        }
        else if (arr_a[idx_a] == arr_b[idx_b]) {
            idx_a++;
            idx_b++;
        }
        else {
            idx_b++;
        }
    }

    cout << res_count << endl;
    for (int i = 0; i < res_count; i++) {
        cout << res[i] << ' ';
    }

    return 0;
}
