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

    int n = 0, start = 0, res = 0;
    cin >> n;

    vector <vector <int>> arr(n + 1, vector <int> (2, 0));
    vector <int> stack;

    for (int i = 0; i < n; ++i) {
        int tmp;
        cin >> tmp;
        arr[i + 1][0] = tmp;
    }
    
    cin >> start;
    stack.push_back(start);
    arr[start][1] = 1;

    while (stack.size()) {
        int top = stack.back();
        stack.pop_back();
        
        if (top - arr[top][0] >= 1 && arr[top - arr[top][0]][1] == 0) {
            arr[top - arr[top][0]][1] = 1;
            stack.push_back(top - arr[top][0]);
        }

        if (top + arr[top][0] <= n && arr[top + arr[top][0]][1] == 0) {
            arr[top + arr[top][0]][1] = 1;
            stack.push_back(top + arr[top][0]);
        }
    }

    for (int i = 0; i < n + 1; ++i) {
        if (arr[i][1] == 1) {
            res++;
        }
    }
    
    cout << res;

    return 0;
}
