// BOJ_1012
// 유기농 배추

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

    int t = 0;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int m, n, k;
        cin >> m >> n >> k;
        
        vector<vector<int>> arr(n + 2, vector<int> (m + 2, 0));
        vector<vector<int>> check(n + 2, vector<int> (m + 2, 0));

        int a, b;
        for (int i = 0; i < k; ++i) {
            cin >> a >> b;
            arr[b + 1][a + 1] = 1;
        }

        for (int i = 0; i < m + 2; ++i) {
            check[0][i] = check[n + 1][i] = 1;
        }
        for (int i = 0; i < n + 2; ++i) {
            check[i][0] = check[i][m + 1] = 1;
        }
        vector<vector<int>> stack(0, vector<int> (2));
        int res = 0;

        for (int j = 1; j < n + 1; ++j) {
            for (int i = 1; i < m + 1; ++i) {
                if (arr[j][i] == 1 && check[j][i] == 0) {
                    stack.push_back({j, i});
                    check[j][i] = 1;
                    res++;

                    while (stack.size()) {
                        vector<int> top(stack.back());
                        stack.pop_back();

                        if (arr[top[0] - 1][top[1]] == 1 && check[top[0] - 1][top[1]] == 0) {
                            check[top[0] - 1][top[1]] = 1;
                            stack.push_back({top[0] - 1, top[1]});
                        }
                        if (arr[top[0] + 1][top[1]] == 1 && check[top[0] + 1][top[1]] == 0) {
                            check[top[0] + 1][top[1]] = 1;
                            stack.push_back({top[0] + 1, top[1]});
                        }
                        if (arr[top[0]][top[1] - 1] == 1 && check[top[0]][top[1] - 1] == 0) {
                            check[top[0]][top[1] - 1] = 1;
                            stack.push_back({top[0], top[1] - 1});
                        }
                        if (arr[top[0]][top[1] + 1] == 1 && check[top[0]][top[1] + 1] == 0) {
                            check[top[0]][top[1] + 1] = 1;
                            stack.push_back({top[0], top[1] + 1});
                        }                                                                             
                    }
                }
            }
        }
        cout << res << '\n';
    }

    return 0;
}