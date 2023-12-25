// BOJ_3049
// 다각형의 대각선

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

    cout << n * (n - 1) * (n - 2) * (n - 3) / 24;

    return 0;
}
