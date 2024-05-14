// 가위_바위_보

function solution(rsp) {
  var answer = '';
  for (let c of rsp) {
    if (c === '2') {
      answer += '0';
    } else if (c === '5') {
      answer += '2';
    } else {
      answer += '5';
    }
  }
  return answer;
}