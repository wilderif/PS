// BOJ_8394
// 악수

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;


int main() {
    int n = 0;
    cin >> n;

<<<<<<< HEAD
    vector<uint64_t> mem(n + 2, 0);
=======
    vector<uint32_t> mem(n + 2, 0);
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    mem[2] = 2;
    mem[3] = 3;

    for (int i = 4; i < n + 1; ++i) {
        mem[i] = (mem[i - 1] + mem[i - 2]) % 10;
    }

    cout << mem[n];

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
