// 배열의_평균값

function solution(numbers) {
    var answer = numbers.reduce((prev, cur) => prev + cur, 0) / numbers.length;
    return answer.toFixed(1);
}