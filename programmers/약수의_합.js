// 약수의_합

function solution(n) {
  var answer = 0;
  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (!(n % i)) {
      if (i === Math.sqrt(n)) {
        answer += i;
      } else {
        answer += i + n / i;
      }
    }
  }

  return answer;
}