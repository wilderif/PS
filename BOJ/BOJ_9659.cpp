// BOJ_9659
// 돌 게임 5

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	uint64_t n = 0;
	cin >> n;

	if (n % 2) {
		cout << "SK";
	} else {
		cout << "CY";
	}

	return 0;
}
