// BOJ_13305
// 주유소

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

    vector<uint64_t> dist(n - 1, 0);
    vector<uint64_t> cost(n, 0);

    for (int i = 0; i < n - 1; i++) {
        cin >> dist[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> cost[i];
        if (i > 0) {
            if (cost[i] > cost[i - 1]) {
                cost[i] = cost[i - 1];
            }
        }
    }

    uint64_t res = 0;
    for (int i = 0; i < n - 1; i++) {
        res += dist[i] * cost[i];
    }

    cout << res;

    return 0;
}