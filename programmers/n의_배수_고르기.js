// n의_배수_고르기

function solution(n, numlist) {
  var answer = [];
  numlist.map((num) => {
    if (num % n === 0) {
      answer.push(num);
    }
  });
  return answer;
}
