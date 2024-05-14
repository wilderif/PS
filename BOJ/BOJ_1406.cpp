// BOJ_1406
// 에디터

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <string>
#include <vector>
#include <list>
#include <utility>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	cin >> s;
	list<char> user_list;
	for (char c : s) {
		user_list.push_back(c);
	}

	int m = 0;
	cin >> m;

	list<char>::iterator cursor = user_list.end();
	while (m--) {		
		char inst;
		cin >> inst;
		if (inst == 'L') {
			if (cursor != user_list.begin()) {
				cursor--;
			}
		} else if (inst == 'D') {
			if (cursor != user_list.end()) {
				cursor++;
			}
		} else if (inst == 'B') {
			if (cursor != user_list.begin()) {
				cursor--;
				cursor = user_list.erase(cursor);
			}
		} else if (inst == 'P') {
			char tmp;
			cin >> tmp;
			user_list.insert(cursor, tmp);
		}
	}

	for (char c : user_list) {
		cout << c;
	}

	return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
