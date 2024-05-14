// BOJ_2578
// 빙고

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    vector<vector<int>> arr(5, vector<int> (5));
    vector<vector<bool>> check(5, vector<bool> (5, false));

    int tmp;
    for (int j = 0; j < 5; ++j) {
        for (int i = 0; i < 5; ++i) {
            cin >> tmp;
            arr[j][i] = tmp;
        }
    }

    int res = 0;
    while (true) {
        int cnt = 0;
        res++;
        cin >> tmp;
        for (int j = 0; j < 5; ++j) {
            for (int i = 0; i < 5; ++i) {
                if (arr[j][i] == tmp) {
                    check[j][i] = true;
                }
            }
        }

        for (int i = 0; i < 5; ++i) {
            if (check[i][i] == false) {
                break;
            }
            if (i == 4) {
                cnt++;
            }
        }

        for (int i = 4; i > -1; --i) {
            if (check[i][5 - i - 1] == false) {
                break;
            }
            if (i == 0) {
                cnt++;
            }
        }

        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                if (check[i][j] == false) {
                    break;
                }
                if (j == 4) {
                    cnt++;
                }
            }
        }

        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                if (check[j][i] == false) {
                    break;
                }
                if (j == 4) {
                    cnt++;
                }
            }     
        }

        if (cnt >= 3) {
            cout << res;
            break;
        }
    }

    return 0;
}