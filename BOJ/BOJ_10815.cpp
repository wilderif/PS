// BOJ_10815
// 숫자 카드

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <limits.h>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;


int main() {
    int n = 0, m = 0;
    set<int> card;
    
    cin >> n;

    for (int i = 0; i < n; ++i) {
        int tmp = 0;
        cin >> tmp;
        card.insert(tmp);
    }

    cin >> m;
    vector<int> res(m, 0);

    for (int i = 0; i < m; ++i) {
        int tmp = 0;
        cin >> tmp;
        if (card.find(tmp) != card.end())
            res[i] = 1;
    }

    for (int i = 0; i < m; ++i) {
        cout << res[i] << ' ';
    }

    return 0;
}
