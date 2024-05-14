// BOJ_10709
// 기상캐스터

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int h, w;
	cin >> h >> w;

	vector<string> arr(h);

	for (int i = 0; i < h; i++) {
		cin >> arr[i];
	}

	bool flag = false;
	int16_t out = -1;
	for (int j = 0; j < h; j++) {
		for (int i = 0; i < w; i++) {
			if (arr[j][i] == 'c') {
				flag = true;
				out = 0;
			}
			cout << out << ' ';
			if (flag) {
				out++;
			}
		}
		out = -1;
		flag = false;
		cout << '\n';
	}

	return 0;
}