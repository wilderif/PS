// 각도기

function solution(angle) {
    var answer = 0;
    if (0 < angle && angle < 90) {
        return 1;
    } else if (angle === 90) {
        return 2;
    } else if (90 < angle && angle < 180) {
        return 3;
    } else {
        return 4;
    }
    return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
