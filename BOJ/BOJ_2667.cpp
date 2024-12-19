// BOJ_2667
// 단지번호붙이기

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <limits.h>
#include <cstdio>

using namespace std;


int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int n;
    cin >> n;

    vector<vector<int>> arr(n + 2, vector<int> (n + 2));
    vector<vector<int>> check(n + 2, vector<int> (n + 2, 0));

    string tmp;
    for (int j = 1; j < n + 1; ++j) {
        cin >> tmp;
        for (int i = 1; i < n + 1; ++i) {
            if (tmp[i - 1] == '0') {
                arr[j][i] = 0;
            }
            else {
                arr[j][i] = 1;
            }
        }
    }

    for (int i = 0; i < n + 2; ++i) {
        check[0][i] = check[n + 1][i] = 1;
        check[i][0] = check[i][n + 1] = 1;
    }

    vector<vector<int>> stack(0, vector<int> (2));
    vector<int> res;
    int res_idx = 0, res_count = 0;

    for (int j = 1; j < n + 1; ++j) {
        for (int i = 1; i < n + 1; ++i) {
            if (arr[j][i] == 1 && check[j][i] == 0) {
                stack.push_back({j, i});
                check[j][i] = 1;
                res_count++;
                res.push_back(1);

                while (stack.size()) {
                    vector<int> top(stack.back());
                    stack.pop_back();

                    if (arr[top[0] - 1][top[1]] == 1 && check[top[0] - 1][top[1]] == 0) {
                        check[top[0] - 1][top[1]] = 1;
                        stack.push_back({top[0] - 1, top[1]});
                        res.back()++;
                    }
                    if (arr[top[0] + 1][top[1]] == 1 && check[top[0] + 1][top[1]] == 0) {
                        check[top[0] + 1][top[1]] = 1;
                        stack.push_back({top[0] + 1, top[1]});
                        res.back()++;
                    }
                    if (arr[top[0]][top[1] - 1] == 1 && check[top[0]][top[1] - 1] == 0) {
                        check[top[0]][top[1] - 1] = 1;
                        stack.push_back({top[0], top[1] - 1});
                        res.back()++;
                    }
                    if (arr[top[0]][top[1] + 1] == 1 && check[top[0]][top[1] + 1] == 0) {
                        check[top[0]][top[1] + 1] = 1;
                        stack.push_back({top[0], top[1] + 1});
                        res.back()++;
                    }                                                                             
                }
            }
        }
    }

    cout << res_count << '\n';
    sort(res.begin(), res.end());
    for (int out : res) {
        cout << out << '\n';
    }

    return 0;
}
