// 자릿수_더하기

function solution(n) {
  var answer = 0;
  while (n) {
    answer += n % 10;
    n = Math.floor(n / 10);
  }
  return answer;
}
