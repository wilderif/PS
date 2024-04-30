// 중복된_숫자_개수

function solution(array, n) {
    var answer = 0;
    array.forEach((val) => {
        if (val === n) {
            answer += 1;
        }
    })
    return answer;
}
