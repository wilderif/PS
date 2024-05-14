// BOJ_16139
// 인간-컴퓨터 상호작용

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	cin >> s;

	vector<vector<uint64_t>> arr(s.size() + 1, vector<uint64_t>(26, 0));

	for (size_t i = 1; i < s.size() + 1; i++) {
		arr[i][s[i - 1] - 'a']++;
		for (int j = 0; j < 26; j++) {
			arr[i][j] += arr[i - 1][j];
		}
	}

	size_t t;
	cin >> t;

	while (t--) {
		char a;
		size_t start, end;
		cin >> a >> start >> end;
		cout << arr[end + 1][a - 'a'] - arr[start][a - 'a'] << '\n';
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
