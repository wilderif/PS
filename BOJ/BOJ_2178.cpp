// BOJ_2178
// 미로 탐색

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

	int n, m;
	cin >> n >> m;

	int dx[4] = {1, 0, -1, 0};
	int dy[4] = {0, 1, 0, -1};

	vector<vector<int>> arr(n, vector<int> (m, 0));
	vector<vector<int>> vis(n, vector<int> (m, 100 * 100));

	for (int j = 0; j < n; j++) {
		string input;
		cin >> input;
		for (int i = 0; i < m; i++) {
			arr[j][i] = input[i] - '0';
		}
	}

	queue<pair<int, int>> q;

	q.push(pair<int, int> {0, 0});
	vis[0][0] = 1;

	while (!q.empty()) {
		pair<int, int> cur = q.front();
		int cur_dis = vis[cur.first][cur.second];
		q.pop();
		for (int i = 0; i < 4; i++) {
			int ny = cur.first + dy[i];
			int nx = cur.second + dx[i];
			if (ny < 0 || ny >= n || nx < 0 || nx >= m) {
				continue;
			}
			if (arr[ny][nx] && vis[ny][nx] > cur_dis + 1) {
				q.push(pair<int, int> {ny, nx});
				vis[ny][nx] = cur_dis + 1;
			}
		}
	}

	cout << vis[n - 1][m - 1];
	
	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
