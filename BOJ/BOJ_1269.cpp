// BOJ_1269
// 대칭 차집합

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int a, b, common_element_count = 0;
    cin >> a >> b;
    set<u_int32_t> set_a;
    set<u_int32_t> set_b;

    int tmp;
    for (int i = 0; i < a; ++i) {
        cin >> tmp;
        set_a.insert(tmp);
    }
    for (int i = 0; i < b; ++i) {
        cin >> tmp;
        set_b.insert(tmp);
    }
    for (auto it = set_a.begin(); it != set_a.end(); ++it) {
        if (set_b.find(*it) != set_b.end()) {
            common_element_count++;
        }
    }

    cout << set_a.size() + set_b.size() - 2 * common_element_count;
    
    return 0;
}