// BOJ_4963
// 섬의 개수

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

    while (1) {
        int w, h;
        cin >> w >> h;
        
        if (w == 0 && h == 0)
            break;

        vector<vector<int>> arr(h + 2, vector<int> (w + 2));
        vector<vector<int>> check(h + 2, vector<int> (w + 2, 0));

        int tmp;
        for (int j = 1; j < h + 1; ++j) {
            for (int i = 1; i < w + 1; ++i) {
                cin >> tmp;
                arr[j][i] = tmp;
            }
        }

        for (int i = 0; i < w + 2; ++i) {
            check[0][i] = check[h + 1][i] = 1;
        }
        for (int i = 0; i < h + 2; ++i) {
            check[i][0] = check[i][w + 1] = 1;
        }

        vector<vector<int>> stack(0, vector<int> (2));
        int res = 0;

        for (int j = 1; j < h + 1; ++j) {
            for (int i = 1; i < w + 1; ++i) {
                if (arr[j][i] == 1 && check[j][i] == 0) {
                    stack.push_back({j, i});
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
                        
                        if (arr[top[0] - 1][top[1] - 1] == 1 && check[top[0] - 1][top[1] - 1] == 0) {
                            check[top[0] - 1][top[1] - 1] = 1;
                            stack.push_back({top[0] - 1, top[1] - 1});
                        }
                        if (arr[top[0] - 1][top[1] + 1] == 1 && check[top[0] - 1][top[1] + 1] == 0) {
                            check[top[0] - 1][top[1] + 1] = 1;
                            stack.push_back({top[0] - 1, top[1] + 1});
                        }
                        if (arr[top[0] + 1][top[1] - 1] == 1 && check[top[0] + 1][top[1] - 1] == 0) {
                            check[top[0] + 1][top[1] - 1] = 1;
                            stack.push_back({top[0] + 1, top[1] - 1});
                        }
                        if (arr[top[0] + 1][top[1] + 1] == 1 && check[top[0] + 1][top[1] + 1] == 0) {
                            check[top[0] + 1][top[1] + 1] = 1;
                            stack.push_back({top[0] + 1, top[1] + 1});
                        }                                                                                                
                    }
                }
            }
        }
        cout << res << '\n';
    }

    return 0;
}