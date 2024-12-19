// BOJ_2923
// 숫자 게임

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

    int n = 0;
    cin >> n;
    int arr_a[100] = {0, };
    int arr_b[100] = {0, };

    for (int i = 0; i < n; ++i) {
        int a, b, idx_a = 1, idx_b = 99, cnt = i + 1, res = 0;
        cin >> a >> b;
        arr_a[a]++;
        arr_b[b]++;

        int tmp_arr_a[100], tmp_arr_b[100];
        copy(begin(arr_a), end(arr_a), begin(tmp_arr_a));
        copy(begin(arr_b), end(arr_b), begin(tmp_arr_b));
        
        while (cnt > 0) {
            while (tmp_arr_a[idx_a] == 0)
                idx_a++;
            while (tmp_arr_b[idx_b] == 0)
                idx_b--;

            res = max(res, idx_a + idx_b);

            if (tmp_arr_a[idx_a] > tmp_arr_b[idx_b]) {
                cnt -= tmp_arr_b[idx_b];
                tmp_arr_a[idx_a] -= tmp_arr_b[idx_b];
                tmp_arr_b[idx_b] = 0;
            }
            else {
                cnt -= tmp_arr_a[idx_a];
                tmp_arr_b[idx_b] -= tmp_arr_a[idx_a];
                tmp_arr_a[idx_a] = 0;
            }
        }
        cout << res << '\n';
    }

    return 0;
}
