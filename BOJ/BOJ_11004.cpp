// BOJ_11004
// K번째 수

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int n, k;
    cin >> n >> k;

    vector<int> arr(n);

    int tmp;
    for (int i = 0; i < n; ++i) {
        cin >> tmp;
        arr[i] = tmp;
    }

    sort(arr.begin(), arr.end());

    cout << arr[k - 1];

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
