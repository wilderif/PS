// BOJ_1092
// 배

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

<<<<<<< HEAD
bool desc(const uint64_t& a, const uint64_t& b) {
=======
bool desc(const uint32_t& a, const uint32_t& b) {
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    return a > b;
}

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
<<<<<<< HEAD
    uint64_t n, m, res = 0;
    cin >> n;
    vector<uint64_t> arr_1(n);
=======
    uint32_t n, m, res = 0;
    cin >> n;
    vector<uint32_t> arr_1(n);
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    for (int i = 0; i < n; ++i) {
        cin >> arr_1[i];
    }

    cin >> m;
<<<<<<< HEAD
    vector<uint64_t> arr_2(m);
=======
    vector<uint32_t> arr_2(m);
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    for (int i = 0; i < m; ++i) {
        cin >> arr_2[i];
    }

    sort(arr_1.begin(), arr_1.end(), desc);
    sort(arr_2.begin(), arr_2.end(), desc);

    if (arr_1[0] < arr_2[0]) {
        cout << -1;
        return 0;
    }

    int i, j;
    while (arr_2.size()) {
        for (i = 0, j = 0; i < n && j < arr_2.size();) {
            if (arr_1[i] >= arr_2[j]) {
                arr_2.erase(arr_2.begin() + j);
                i++;
            } else {
                j++;
            }
        }
        res++;
    }
    cout << res;

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
