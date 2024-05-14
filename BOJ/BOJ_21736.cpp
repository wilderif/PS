// BOJ_21736
// 헌내기는 친구가 필요해

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;

    vector<vector<char>> arr(n + 2, vector<char> (m + 2, 'X'));
    vector<vector<bool>> check(n + 2, vector<bool> (m + 2, false));
    vector<vector<int>> stack(0, vector<int>(2, 0));

    int arr_x[4] = {1, -1, 0, 0};
    int arr_y[4] = {0, 0, 1, -1};
    
    char tmp;
    for (int j = 1; j < n + 1; ++j) {
        for (int i = 1; i < m + 1; ++i) {
            cin >> tmp;
            arr[j][i] = tmp;
            if (tmp == 'I') {
                stack.push_back(vector<int> {j, i});
            }
        }
    }

    int res = 0;
    while (stack.size()) {
        vector<int> tmp = stack.back();
        stack.pop_back();
        for (int i = 0; i < 4; ++i) {
            if (arr[tmp[0] + arr_y[i]][tmp[1] + arr_x[i]] == 'P' && !check[tmp[0] + arr_y[i]][tmp[1] + arr_x[i]]) {
                res += 1;
                stack.push_back(vector<int> {tmp[0] + arr_y[i], tmp[1] + arr_x[i]});
                check[tmp[0] + arr_y[i]][tmp[1] + arr_x[i]] = 1;
            } else if (arr[tmp[0] + arr_y[i]][tmp[1] + arr_x[i]] == 'O' && !check[tmp[0] + arr_y[i]][tmp[1] + arr_x[i]]) {
                stack.push_back(vector<int> {tmp[0] + arr_y[i], tmp[1] + arr_x[i]});
                check[tmp[0] + arr_y[i]][tmp[1] + arr_x[i]] = 1;
            }
        }
    }

    if (res)
        cout << res;
    else
        cout << "TT";
   
    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
