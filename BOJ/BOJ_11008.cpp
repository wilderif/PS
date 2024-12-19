// BOJ_11008
// 복붙의 달인

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

    int t = 0;
    cin >> t;
    
    while (t--) {
        string s, p;
        cin >> s >> p;
        
        int idx = 0, res = 0;
        while (idx < s.size() - p.size() + 1) {
            for (int i = 0; i < p.size(); ++i) {
                if (p[i] != s[i + idx]) {
                    res++;
                    idx++;
                    break;
                }
                if (i == p.size() - 1) {
                    idx += p.size();
                    res++;
                }
            }
        }
        res += s.size() - idx;
        cout << res << '\n';
    }

    return 0;
}
