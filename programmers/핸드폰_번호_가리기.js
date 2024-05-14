// 핸드폰_번호_가리기

function solution(phone_number) {
  var answer = '';
  let arr = Array.from(phone_number);
  arr = [...(new Array(arr.length - 4).fill('*')), ...arr.slice(arr.length - 4, arr.length)];
  console.log(arr);
  answer = arr.join('');
  return answer;
}