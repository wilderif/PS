// BOJ_11815
// 짝수? 홀수?

#include <iostream>
#include <cmath>

using namespace std;


int main() {
    int n = 0;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        unsigned long long tmp;
        cin >> tmp;
        unsigned long long root = static_cast<unsigned long long>(sqrt(tmp));
        if (root * root == tmp)
            cout << 1 << ' ';
        else
            cout << 0 << ' ';        
    }

    return 0;
}
