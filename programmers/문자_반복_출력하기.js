// 문자_반복_출력하기

function solution(my_string, n) {
    var answer = '';
    for (let c of my_string) {
        for (let i = 0; i < n; i++) {
            answer += c;
        }
    }
    return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
