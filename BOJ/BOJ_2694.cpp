// BOJ_2694
// 합이 같은 구간

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int t = 0;
	cin >> t;
	
	while (t--) {
		int m = 0;
		cin >> m;

		vector<int> arr(m, 0);
		for (int i = 0; i < m; i++) {
			cin >> arr[i];
			if (i) {
				arr[i] += arr[i - 1];
			}
		}

		int target = 0;
		for (int i = 0; i < m; i++) {
			target = arr[i];
			if (arr[m - 1] % target) {
				continue;
			}
			int idx1 = i, idx2 = i;
			bool flag = false;
			while (true) {
				if (idx2 == m) {
					break;
				}
				if (arr[idx2] - arr[idx1] == target) {
					if (idx2 == m - 1) {
						cout << target << '\n';
						flag = true;
						break;
					}
					idx1 = idx2;
				}
				idx2++;
			}
			if (flag) {
				break;
			}
			if (i == m - 1) {
				cout << target << '\n';
			}
		}
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
