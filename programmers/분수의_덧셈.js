// 분수의_덧셈

function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    let res2 = Math.floor(denom1 * denom2 / gcd(denom1, denom2));
    let res1 = Math.floor(numer1 * (res2 / denom1)) + Math.floor(numer2 * (res2 / denom2));
    let tmp = gcd(res1, res2);
    res1 = Math.floor(res1 / tmp);
    res2 = Math.floor(res2 / tmp);
    answer.push(res1);
    answer.push(res2);
    return answer;
}

const gcd = (num1, num2) => {
    if (num2 === 0) {
        return num1;
    }
    return gcd(num2, num1 % num2);
}
