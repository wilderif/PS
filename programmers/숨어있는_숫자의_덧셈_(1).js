// 숨어있는_숫자의_덧셈_(1)

function solution(my_string) {
  var answer = 0;
  for (let c of my_string) {
    if (!isNaN(c)) {
      answer += parseInt(c);
    }
  }

  return answer;
}
