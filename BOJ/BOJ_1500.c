// BOJ_1500
// 최대 곱

#include <stdio.h>

int main()
{
    int s, k;
    long long res = 1;
    scanf("%d %d", &s, &k);

    int arr[20];
    for (int i = 0; i < k; ++i) {
        arr[i] = 1;
    }
    for (int i = 0; i < k; ++i) {
        arr[i] = s / k;
    }

    for (int i = 0; i < s % k; ++i) {
        arr[i]++;
    }

    for (int i = 0; i < k; ++i) {
        res *= arr[i];
    }

    printf("%lld", res);

    return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
