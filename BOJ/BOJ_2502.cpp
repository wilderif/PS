// BOJ_2502
// 떡 먹는 호랑이

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;


int main() {
    int d, k, a = 1, b = 1;
    cin >> d >> k;
    vector<vector<int>> mem(d + 3, vector<int>(2, 0));

    mem[1][0] = 1;
    mem[2][1] = 1;

    for (int i = 3; i < d + 1; ++i) {
        mem[i][0] = mem[i - 1][0] + mem[i - 2][0];
        mem[i][1] = mem[i - 1][1] + mem[i - 2][1];
    }

    while (true) {
        if (mem[d][0] * a + mem[d][1] * b == k) {
            cout << a << '\n' << b;
            break;
        }
        else if (mem[d][0] * a + mem[d][1] * b < k) {
            b++;
        }
        else {
            a++;
            b = 1;
        }
    }

    return 0;
}