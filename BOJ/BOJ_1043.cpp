// BOJ_1043
// 거짓말

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
    
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> party(m, vector<bool> (n + 1, false));
    vector<vector<bool>> check(m, vector<bool> (n + 1, false));

    int know_num = 0;
    cin >> know_num;
    vector<int> know(know_num, 0);
    for (int i = 0; i < know_num; ++i) {
        cin >> know[i];
    }

    int tmp_1;
    int tmp_2;
    for (int i = 0; i < m; ++i) {
        check[i][0] = true;
        cin >> tmp_1;
        for (int j = 0; j < tmp_1; ++j) {
            cin >> tmp_2;
            party[i][tmp_2] = true;
        }
    }

    int tmp;
    while (know.size()) {
        tmp = know[know.size() - 1];
        know.pop_back();
        for (int i = 0; i < m; ++i) {
            if (party[i][tmp] && !check[i][tmp]) {
                if (check[i][0]) {
                    check[i][0] = false;
                }
                check[i][tmp] = true;
                for (int j = 1; j < n + 1; ++j) {
                    if (party[i][j] && !check[i][j]) {
                        check[i][j] = true;
                        know.push_back(j);
                    }
                }
            }
        }
    }
    
    int res = 0;
    for (int i = 0; i < m; ++i) {
        if (check[i][0]) {
            res++;
        }
    }
    cout << res;

    return 0;
}