// BOJ_1926
// 그림

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
	vector<vector<bool>> vis(n, vector<bool> (m, false));

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < m; i++) {
			cin >> arr[j][i];
		}
	}

	queue<pair<int, int>> q;

	int cnt = 0;
	int largest = 0;

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < m; i++) {
			int tmp_size = 0;
			if (arr[j][i] && !vis[j][i]) {
				q.push(pair<int, int> {j, i});
				vis[j][i] = true;
				cnt++;
				tmp_size++;
			}
			while (!q.empty()) {
				pair<int, int> cur = q.front();
				q.pop();
				for (int k = 0; k < 4; k++) {
					int ny = cur.first + dy[k];
					int nx = cur.second + dx[k];
					if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
						continue;
					}
					if (arr[ny][nx] && !vis[ny][nx]) {
						q.push(pair<int, int> {ny, nx});
						vis[ny][nx] = true;
						tmp_size++;
					}
				}
			}
			largest = max(largest, tmp_size);
		}
	}
	
	cout << cnt << '\n';
	cout << largest << '\n';

	return 0;
}