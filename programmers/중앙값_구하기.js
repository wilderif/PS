// 중앙값_구하기

function solution(array) {
    var answer = 0;
    array.sort((a, b) => a - b);
    answer = array[Math.floor(array.length / 2)];
    return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
