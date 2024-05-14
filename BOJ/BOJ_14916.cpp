// BOJ_14916
// 거스름돈

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n = 0;
	cin >> n;

	vector<int> mem(n + 10, -1);
	mem[2] = mem[5] = 1;
	mem[4] = 2;

	for (int i = 6; i < n + 1; i++) {
		if (mem[i - 5] != -1 && mem[i - 2] != - 1) {
			mem[i] = min(mem[i - 5], mem[i - 2]) + 1;
		}
		if (mem[i - 5] != -1 && mem[i - 2] == - 1) {
			mem[i] = mem[i - 5] + 1;
		}
		if (mem[i - 5] == -1 && mem[i - 2] != - 1) {
			mem[i] = mem[i - 2] + 1;
		}
	}

	cout << mem[n];

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
