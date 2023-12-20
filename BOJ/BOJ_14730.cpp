// BOJ_14730
// 謎紛芥索紀 (Small)

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
    
    int res = 0;
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        res += a * b;
    }

    cout << res;

    return 0;
}
