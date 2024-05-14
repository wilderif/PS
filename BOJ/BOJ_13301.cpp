// BOJ_13301
// 타일 장식물

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
    if (n == 1) {
        cout << 4;
        return 0;
    }

    vector<uint64_t> mem(n + 2, 0);
    mem[1] = 1;
    mem[2] = 1;

    for (int i = 3; i < n + 1; i++) {
        mem[i] = mem[i - 1] + mem[i - 2];
    }

    uint64_t res = (mem[n] + mem[n - 1] + mem[n - 1] + mem[n - 2]) * 2;
    cout << res;

    return 0;
}