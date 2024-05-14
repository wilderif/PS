// BOJ_6588
// 골드바흐의 추측

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    vector<bool> arr(1000001, true);
    for (size_t i = 2; i < arr.size(); i++) {
        if (arr[i]) {
            for (size_t j = 2; i * j < arr.size(); j++) {
                arr[i * j] = false;
            }
        }
    }

    while (true) {
        uint64_t n = 0;
        cin >> n;

        if (!n) {
            break;
        }

        uint64_t idx1 = 3, idx2 = n;
        while (true) {
            while (!arr[idx1]) {
                idx1++;
            }
            while (!arr[idx2]) {
                idx2--;
            }

            if (idx1 + idx2 > n) {
                idx2--;
            } else if (idx1 + idx2 == n) {
                cout << n << " = " << idx1 << " + " << idx2 << '\n';
                break;
            } else {
                idx1++;
            }

            if (idx1 > idx2) {
                cout << "Goldbach's conjecture is wrong.\n";
                break;
            }
        }
    }

    return 0;
}