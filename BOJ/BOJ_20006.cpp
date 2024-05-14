// BOJ_20006
// 랭킹전 대기열

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

bool compare(const pair<int, string> &a, const pair<int, string> &b) {
	return a.second < b.second;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int p, m;
	cin >> p >> m;

	vector<vector<pair<int, string>>> q;

	for (size_t i = 0; i < p; i++) {
		int tmp1 = 0;
		string tmp2 = "";
		cin >> tmp1 >> tmp2;

		bool create_flag = true;
		for (size_t j = 0; j < q.size(); j++) {
			if (q[j][0].first - 10 <= tmp1 && tmp1 <= q[j][0].first + 10 && q[j].size() < m) {
				create_flag = false;
				q[j].push_back(make_pair(tmp1, tmp2));
				break;
			}
		}
		if (create_flag) {
			q.push_back(vector<pair<int, string>> {make_pair(tmp1, tmp2)});
		}
	}

	for (vector<pair<int, string>> tmp_vec : q) {
		sort(tmp_vec.begin(), tmp_vec.end(), compare);
		if (tmp_vec.size() == m) {
			cout << "Started!\n";
		} else {
			cout << "Waiting!\n";
		}
		for (pair<int, string> tmp_pair : tmp_vec) {
			cout << tmp_pair.first << ' ' << tmp_pair.second << '\n';
		}
	}

	return 0;
}