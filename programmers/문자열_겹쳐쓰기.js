// 문자열_겹쳐쓰기

function solution(my_string, overwrite_string, s) {
    var answer = '';
    let arr = [...my_string];
    let idx = s;
    for (let c of overwrite_string) {
        arr[s++] = c;
    }
    answer = arr.join('');
    return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
