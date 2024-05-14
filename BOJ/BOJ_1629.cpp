// BOJ_1629
// 곱셈

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>

using namespace std;

uint64_t pow(uint64_t a, uint64_t b, uint64_t c) {
	if (b == 1) {
		return a % c;
	}
	
	if (b % 2) {
		return ((pow(a, b / 2, c) * pow(a, b / 2, c)) % c * (a % c)) % c;
	} else {
		return (pow(a, b / 2, c) * pow(a, b / 2, c)) % c;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	uint64_t a, b, c;
	cin >> a >> b >> c;

	cout << pow(a, b, c);

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
