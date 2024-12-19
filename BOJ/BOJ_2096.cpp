// BOJ_2096
// 내려가기

#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unsigned int n;
    cin >> n;
    

    unsigned int max_res = 0;
    unsigned int min_res = UINT32_MAX;
    
    unsigned int max_mem[2][5];
    unsigned int min_mem[2][5];

    for (int j = 0; j < 2; ++j) {
        max_mem[j][0] = 0;
        max_mem[j][4] = 0;
        min_mem[j][0] = UINT32_MAX;
        min_mem[j][4] = UINT32_MAX;

        for (int i = 1; i < 4; ++i) {
            unsigned int tmp;
            cin >> tmp;
            max_mem[j][i] = min_mem[j][i] = tmp;
        }
        
        if (n == 1) {
            for (int i = 1; i < 4; ++i) {
                if (max_mem[0][i] > max_res) {
                    max_res = max_mem[0][i];
                }
                if (min_mem[0][i] < min_res) {
                    min_res = min_mem[0][i];
                }
            }
            cout << max_res << ' ' << min_res;
            return 0;        
        }        
    }

    for (int j = 0; j < n - 1; ++j) {
        for (int i = 1; i < 4; ++i) { 
            max_mem[1][i] += max(max(max_mem[0][i - 1], max_mem[0][i]), max_mem[0][i + 1]);
            min_mem[1][i] += min(min(min_mem[0][i - 1], min_mem[0][i]), min_mem[0][i + 1]);
        }

        if (j == n - 2)
            break;

        for (int i = 1; i < 4; ++i) {
            max_mem[0][i] = max_mem[1][i];
            min_mem[0][i] = min_mem[1][i];
            unsigned int tmp;
            cin >> tmp;
            max_mem[1][i] = min_mem[1][i] = tmp;
        }

        max_mem[1][0] = 0;
        max_mem[1][4] = 0;
        min_mem[1][0] = UINT32_MAX;
        min_mem[1][4] = UINT32_MAX;
    }

    for (int i = 1; i < 4; ++i) {
        if (max_mem[1][i] > max_res) {
            max_res = max_mem[1][i];
        }
        if (min_mem[1][i] < min_res) {
            min_res = min_mem[1][i];
        }
    }

    cout << max_res << ' ' << min_res;
    
    return 0;
}
