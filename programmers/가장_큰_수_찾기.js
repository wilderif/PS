// 가장_큰_수_찾기

function solution(array) {
  var answer = [];
  answer = [array[0], 0];
  for (let i = 0; i < array.length; i++) {
    if (array[i] > answer[0]) {
      answer[0] = array[i];
      answer[1] = i;
    }
  }
  return answer;
}
