// BOJ_5347
// LCM

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 0;
    cin >> n;

    while (n--) {
        uint64_t a, b;
        cin >> a >> b;

        uint64_t for_d = 1;
        if (a <= b) {
            for (int i = 1; i < a + 1; i++) {
                if (a % i == 0 && b % i == 0) {
                    for_d = i;
                }
            }
        } else {
            for (int i = 1; i < b + 1; i++){
                if (a % i == 0 && b % i == 0) {
                    for_d = i;
                }
            }
        }

        cout << a * b / for_d << '\n';
    }

    return 0;
} 
