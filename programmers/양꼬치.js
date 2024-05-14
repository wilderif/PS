// 양꼬치

function solution(n, k) {
    var answer = 0;
    k -= Math.floor(n / 10);
    k = k < 0 ? 0 : k;
    answer = n * 12000 + k * 2000;
    return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
