// BOJ_1309
// 동물원

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);
    
    uint64_t n;
    cin >> n;

    vector<uint64_t> mem(n + 2, 0);
    mem[1] = 3;
    mem[2] = 7;

    for (int i = 3; i < n + 1; ++i) {
        mem[i] = mem[i - 1] * 2 + mem[i - 2];
        mem[i] %= 9901;
    }

    cout << mem[n];
    
    return 0;
}