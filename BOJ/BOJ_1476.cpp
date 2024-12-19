// BOJ_1476
// 날짜 계산

#include <iostream>
#include <cstdint>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int e = 1, s = 1, m = 1, res = 1;
    int e_in, s_in, m_in;
    cin >> e_in >> s_in >> m_in;

    while (true) {
        if (e == e_in && s == s_in && m == m_in) {
            break;
        }
        e %= 15;
        e++;
        s %= 28;
        s++;
        m %= 19;
        m++;
        res++;
    }

    cout << res;

    return 0;
}
