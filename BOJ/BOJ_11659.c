// BOJ_11659
// 구간 합 구하기 4

#include <stdio.h>

int main()
{
    int n, m, s, e;
    scanf("%d %d", &n, &m);
    int num_arr[n];

    for (int i = 0; i < n; ++i)
        scanf("%d ", &num_arr[i]);

    for (int i = 1; i < n; ++i)
        num_arr[i] = num_arr[i] + num_arr[i - 1];

    for (int i = 0; i < m; ++i){
        scanf("%d %d", &s, &e);
        if (s == 1)
            printf("%d\n", num_arr[e - 1]);
        else
            printf("%d\n", num_arr[e - 1] - num_arr[s - 2]);
    }

    return 0;
}
