// BOJ_1422
// 숫자의 신

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(string a, string b) {
    return a + b > b + a;
}

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int k, n;
<<<<<<< HEAD
    uint64_t biggest = 0;
=======
    uint32_t biggest = 0;
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    cin >> k >> n;
    vector<string> arr;
    
    string tmp;
<<<<<<< HEAD
    uint64_t int_tmp;
=======
    uint32_t int_tmp;
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    for (int i = 0; i < k; ++i) {
        cin >> tmp;
        int_tmp = stoi(tmp);
        biggest = max(int_tmp, biggest);
        arr.push_back(tmp);
    }

    for (int i = 0; i < n - k; ++i) {
        arr.push_back(to_string(biggest));
    }

    sort(arr.begin(), arr.end(), compare);

    for (int i = 0; i < arr.size(); ++i) {
        cout << arr[i];
    }
      
    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
