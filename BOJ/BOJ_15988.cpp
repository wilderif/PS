// BOJ_15988
// 1, 2, 3 더하기 3

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    uint64_t mem[1000001] = {0, };

    mem[1] = 1;
    mem[2] = 2;
    mem[3] = 4;

    for (int i = 4; i < 1000001; i++) {
        mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3];
        mem[i] %= 1000000009;
    }

    int t;
    cin >> t;
    while (t--) {
        int tmp;
        cin >> tmp;
        cout << mem[tmp] << '\n';
    }

    return 0;
}