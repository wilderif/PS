// BOJ_4948
// 베르트랑 공준

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

	vector<bool> prime(123456 * 2 + 1, true);
	vector<int> prime_count(123456 * 2 + 1, 0);

	for (int i = 2; i < 123456 * 2 + 1; i++) {
		if (prime[i]) {
			for (int j = 2; j * i < 123456 * 2 + 1; j++) {
				prime[i * j] = false;
			}
		}
	}

	int cur = 0;
	for (int i = 2; i < prime_count.size(); i++) {
		if (prime[i]) {
			cur++;
		}
		prime_count[i] = cur;
	}

	while (true) {
		int n = 0;
		cin >> n;

		if (!n) {
			break;
		} else {
			cout << prime_count[n * 2] - prime_count[n] << '\n';
		}
	}

	return 0;
}