// BOJ_2477
// 참외밭

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int n = 0;
    cin >> n;

    vector<vector<int>> arr(6, vector<int> (2, 0));
    vector<int> count_direction(5, 0);

    int d, l;
    for (int i = 0; i < 6; ++i) {
        cin >> d >> l;
        count_direction[d]++;
        arr[i][0] = d;
        arr[i][1] = l;
    }

    while (count_direction[arr[0][0]] != 1 || count_direction[arr[1][0]] != 1) {
        vector<int> tmp = arr[0];
        arr.erase(arr.begin());
        arr.push_back(tmp);
    }

    int total = arr[0][1] * arr[1][1] - arr[3][1] * arr[4][1];

    cout << total * n;

    return 0;
}
