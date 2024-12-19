// 머쓱이보다_키_큰_사람

function solution(array, height) {
  var answer = 0;
  answer = array.filter((item) => {
    return item > height;
  }).length;
  return answer;
}
