// BOJ_9507
// Generations of Tribbles

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <limits.h>
#include <cstdio>

using namespace std;


int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int t = 0;
    cin >> t;

    vector<long long> mem(68, 0);

    mem[0] = 1;
    mem[1] = 1;
    mem[2] = 2;
    mem[3] = 4;

    for (int i = 4; i < 69; ++i) {
        mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3] + mem[i - 4];
    }

    for (int i = 0; i < t; ++i) {
        int tmp;
        cin >> tmp;
        cout << mem[tmp] << '\n';
    }

    return 0;
}
