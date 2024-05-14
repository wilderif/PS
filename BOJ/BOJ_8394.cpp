// BOJ_8394
// 악수

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;


int main() {
    int n = 0;
    cin >> n;

    vector<uint64_t> mem(n + 2, 0);
    mem[2] = 2;
    mem[3] = 3;

    for (int i = 4; i < n + 1; ++i) {
        mem[i] = (mem[i - 1] + mem[i - 2]) % 10;
    }

    cout << mem[n];

    return 0;
}