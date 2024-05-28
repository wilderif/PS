// 문자열_정렬하기_(1)

function solution(my_string) {
  var answer = [];
  answer = my_string
    .split("")
    .filter((el) => {
      return !isNaN(el);
    })
    .map((el) => Number(el));
  return answer.sort((a, b) => a - b);
}
