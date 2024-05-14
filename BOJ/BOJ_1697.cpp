// BOJ_1697
// 숨바꼭질

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, k;
	cin >> n >> k;
	vector<int> vis(100001, INT32_MAX);

	queue<int> q;
	q.push(n);
	vis[n] = 0;

	while (vis[k] == INT32_MAX) {
		int cur = q.front();
		int cur_dis = vis[cur];
		q.pop();
		if (cur - 1 >= 0 && vis[cur - 1] > cur_dis + 1) {
			q.push(cur - 1);
			vis[cur - 1] = cur_dis + 1;
		}
		if (cur + 1 <= 100001 && vis[cur + 1] > cur_dis + 1) {
			q.push(cur + 1);
			vis[cur + 1] = cur_dis + 1;
		}
		if (cur * 2 <= 100001 && vis[cur * 2] > cur_dis + 1) {
			q.push(cur * 2);
			vis[cur * 2] = cur_dis + 1;
		}
	}

	cout << vis[k];

	return 0;
}