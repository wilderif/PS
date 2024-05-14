// 세균_증식

function solution(n, t) {
  var answer = 0;
  answer = n;
  while (t--) {
    answer *= 2;
  }
  return answer;
}
