// BOJ_5800
// 성적 통계

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <string>

using namespace std;


int main() {
    int k = 0;
    cin >> k;

    for (int i = 0; i < k; ++i) {
        int n = 0, gap = 0;
        cin >> n;
        vector<int> score(n);

        for (int j = 0; j < n; ++j) {
            int tmp = 0;
            cin >> tmp;
            score[j] = tmp;
        }
        sort(score.begin(), score.end());

        for (int j = 1; j < n; ++j) {
            if (score[j] - score[j - 1] > gap) {
                gap = score[j] - score[j - 1];
            }
        }

        cout << "Class " << i + 1 << '\n';
        cout << "Max " << score[n - 1] << ", ";
        cout << "Min " << score[0] << ", ";
        cout << "Largest gap " << gap << '\n';
    }

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
